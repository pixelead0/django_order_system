import logging

from django.db import models
from django.utils.translation import ugettext_lazy as _

from app.core.models import SaveReversionMixin, TimestampMixin
from app.main.models import Supplier

logger = logging.getLogger(__name__)


class Article(SaveReversionMixin, TimestampMixin):
    """Article catalog."""

    name = models.CharField(
        verbose_name=_("Descripción"),
        help_text=_("Descripción del artículo"),
        max_length=100,
        null=False,
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0.00,
    )

    code = models.CharField(
        verbose_name=_("Código"),
        help_text=_("Número de artículo"),
        max_length=30,
        null=False,
    )

    supplier = models.ManyToManyField(
        Supplier,
        verbose_name=_("Proveedor"),
        blank=True,
    )

    class Meta:
        verbose_name = _("Artículo")
        verbose_name_plural = _("Artículos")
        # ordering = ["-updated_at"]

    def __str__(self):
        return f"{self.name}"
