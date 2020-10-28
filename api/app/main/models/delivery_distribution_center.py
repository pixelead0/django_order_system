import logging

from app.core.models import SaveReversionMixin, TimestampMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

logger = logging.getLogger(__name__)


class DeliveryDistributionCenter(SaveReversionMixin, TimestampMixin):
    """Delivering to distribution center catalog."""

    name = models.CharField(
        verbose_name=_("Almacén"),
        help_text=_("Nombre del almacén"),
        max_length=250,
    )

    class Meta:
        verbose_name = _("Entrega en Centro de distribución")
        verbose_name_plural = _("Entregas en centro de distribución")

    def __str__(self):
        return f"{self.name}"
