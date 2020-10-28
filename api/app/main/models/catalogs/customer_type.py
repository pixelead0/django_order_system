import logging

from app.core.models import SaveReversionMixin, TimestampMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

logger = logging.getLogger(__name__)


class CustomerType(SaveReversionMixin, TimestampMixin):
    """Customer type catalog."""

    name = models.CharField(
        verbose_name=_("Tipo de cliente"),
        max_length=512,
        default="",
    )

    class Meta:
        verbose_name = _("Tipo de cliente")
        verbose_name_plural = _("Tipos de cliente")

    def __str__(self):
        return f"{self.name}"
