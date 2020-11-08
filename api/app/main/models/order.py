import logging
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

from app.core.models import SaveReversionMixin, TimestampMixin
from app.main.models import Customer
from app.main.models import DeliveryAssociateCompany
from app.main.models import DeliveryBranchOffice
from app.main.models import DeliveryDistributionCenter
from app.main.constants import DeliveryChoices


logger = logging.getLogger(__name__)


class Order(SaveReversionMixin, TimestampMixin):
    """Orders for items."""

    number = models.PositiveIntegerField(
        verbose_name=_("Orden"),
        help_text=_("Número de orden"),
        unique=True,
    )

    customer = models.ForeignKey(
        Customer,
        verbose_name=_("Cliente"),
        default=None,
        null=True,
        on_delete=models.PROTECT,
    )

    is_urgent = models.BooleanField(
        verbose_name=_("¿Pedido urgente?"),
        default=False,
    )

    is_delivered = models.BooleanField(
        verbose_name=_("¿Pedido entregado?"),
        default=False,
    )

    delivered_at = models.DateTimeField(
        verbose_name=_("Fecha de entrega"),
        blank=True,
        default=None,
        null=True,
    )

    delivery_type = models.PositiveIntegerField(
        verbose_name=_("Lugar de entrega"),
        null=False,
        choices=DeliveryChoices.DELIVERY_CHOICES,
    )

    delivery_associate_company = models.ForeignKey(
        DeliveryAssociateCompany,
        verbose_name=_("Entrega a empresa Asociada"),
        default=None,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )

    delivery_branch_office = models.ForeignKey(
        DeliveryBranchOffice,
        verbose_name=_("Entrega a sucursal"),
        default=None,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )

    delivery_distribution_center = models.ForeignKey(
        DeliveryDistributionCenter,
        verbose_name=_("Entrega a centro de distribución"),
        default=None,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = _("Pedido")
        verbose_name_plural = _("Pedidos")

    def __str__(self):
        return f"{self.number}"


@receiver(pre_save, sender=Order)
def pre_save_validate_delivery(sender, instance, **kwargs):
    """Validate of the selected place of delivery."""
    delivery_type = instance.delivery_type
    # logger.info(delivery_type)

    if delivery_type == DeliveryChoices.DELIVERY_ASSOCIATE_COMPANY:
        if not instance.delivery_associate_company:
            raise ValidationError(
                _("Se requiere empresa asociada de entrega"),
            )
        instance.delivery_distribution_center = None
        instance.delivery_branch_office = None

    elif delivery_type == DeliveryChoices.DELIVERY_BRANCH_OFFICE:
        if not instance.delivery_branch_office:
            raise ValidationError(
                _("Se requiere sucursal de entrega"),
            )
        instance.delivery_associate_company = None
        instance.delivery_distribution_center = None

    elif delivery_type == DeliveryChoices.DELIVERY_DISTRIBUTION_CENTER:
        if not instance.delivery_distribution_center:
            raise ValidationError(
                _("Se requiere centro de distribución de entrega"),
            )
        instance.delivery_associate_company = None
        instance.delivery_branch_office = None
