import logging

from app.core.models import SaveReversionMixin, TimestampMixin
from django.db import models
from app.main.models import Order, Article
from django.utils.translation import ugettext_lazy as _

logger = logging.getLogger(__name__)


class OrderDetail(SaveReversionMixin, TimestampMixin):
    """OrderDetail catalog."""

    order = models.ForeignKey(
        Order,
        verbose_name=_("Orden"),
        null=False,
        on_delete=models.PROTECT,
    )

    article = models.ForeignKey(
        Article,
        verbose_name=_("Artículo"),
        null=False,
        on_delete=models.PROTECT,
    )

    qty = models.PositiveIntegerField(
        verbose_name=_("Cantidad"),
        help_text=_("Cantidad a ordenar"),
    )

    class Meta:
        verbose_name = _("Pedido - Detalle")
        verbose_name_plural = _("Pedidos - Detalle")

    def __str__(self):
        return f"{self.order.number}"
