import logging
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from app.core.models import (SaveReversionMixin, TimestampMixin,
                             UploadFileConfig)
from app.main.models import CustomerType

logger = logging.getLogger(__name__)


upload_path = "uploads/customers/"
photo_filemame = UploadFileConfig(upload_path, "photo")


class Customer(SaveReversionMixin, TimestampMixin):
    """Customer catalog."""

    name = models.CharField(
        verbose_name=_("Nombre"),
        help_text=_("Nombre del cliente"),
        max_length=100,
        null=False,
    )

    code = models.CharField(
        verbose_name=_("Código"),
        help_text=_("Número de cliente"),
        max_length=30,
        null=False,
        unique=True,
    )

    photo = models.ImageField(
        verbose_name=_("Foto"),
        help_text=_("Selecciona o arrastra una foto aquí"),
        upload_to=photo_filemame,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["jpg", "png", "svg"],
            )
        ],
        default=None,
        null=True,
    )

    customer_type = models.ForeignKey(
        CustomerType,
        verbose_name=_("Tipo de cliente"),
        null=False,
        on_delete=models.PROTECT,
    )

    @property
    def customer_type_name(self):
        """Return the name for customer type."""
        return self.customer_type.name

    class Meta:
        verbose_name = _("Cliente")
        verbose_name_plural = _("Clientes")
        # ordering = ["-updated_at"]

    def __str__(self):
        return f"{self.name}"
