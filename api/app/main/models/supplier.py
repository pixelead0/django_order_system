import logging

from app.core.models import SaveReversionMixin, TimestampMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

logger = logging.getLogger(__name__)


class Supplier(SaveReversionMixin, TimestampMixin):
    """Supplier catalog."""

    name = models.CharField(
        verbose_name=_("Nombre"),
        help_text=_("Nombre del proveedor"),
        max_length=50,
        default="",
    )

    address = models.CharField(
        verbose_name=_("Dirección"),
        help_text=_("Dirección del proveedor"),
        max_length=250,
        default="",
    )

    class Meta:
        verbose_name = _("Proveedor")
        verbose_name_plural = _("Proveedores")

    def __str__(self):
        return f"{self.name}"
