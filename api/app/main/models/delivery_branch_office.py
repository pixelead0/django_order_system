import logging

from django.db import models
from django.utils.translation import ugettext_lazy as _

from app.core.models import SaveReversionMixin, TimestampMixin

logger = logging.getLogger(__name__)


class DeliveryBranchOffice(SaveReversionMixin, TimestampMixin):
    """Delivering to branch office catalog."""

    name = models.CharField(
        verbose_name=_("Nombre"),
        help_text=_("Nombre de la sucursal"),
        max_length=50,
        default="",
    )

    reference = models.CharField(
        verbose_name=_("Referencia"),
        help_text=_("Referencia de la sucursal"),
        max_length=250,
        default="",
    )
    code = models.PositiveIntegerField(
        verbose_name=_("Código"),
        help_text=_("Código de la sucursal"),
        unique=True,
    )

    class Meta:
        verbose_name = _("Entrega en sucursal")
        verbose_name_plural = _("Entregas en sucursal")

    def __str__(self):
        return f"{self.name}"
