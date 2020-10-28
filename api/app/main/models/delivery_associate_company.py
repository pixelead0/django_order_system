import logging

from app.core.models import SaveReversionMixin, TimestampMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

logger = logging.getLogger(__name__)


class DeliveryAssociateCompany(SaveReversionMixin, TimestampMixin):
    """Delivering to associate company catalog."""

    name = models.CharField(
        verbose_name=_("Nombre"),
        help_text=_("Nombre de la empresa asociada"),
        max_length=50,
        default="",
    )

    reference = models.CharField(
        verbose_name=_("Referencia"),
        help_text=_("Referencia de la empresa asociada"),
        max_length=250,
        default="",
    )

    code = models.PositiveIntegerField(
        verbose_name=_("Código"),
        help_text=_("Código del socio"),
        unique=True,
    )

    class Meta:
        verbose_name = _("Entrega en empresa asociada")
        verbose_name_plural = _("Entregas en empresa asociada")

    def __str__(self):
        return f"{self.name}"
