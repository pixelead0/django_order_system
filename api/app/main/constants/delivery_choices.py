from django.utils.translation import ugettext_lazy as _


class DeliveryChoices:
    """Choices for delivery an order."""

    DELIVERY_DISTRIBUTION_CENTER = 1
    DELIVERY_BRANCH_OFFICE = 2
    DELIVERY_ASSOCIATE_COMPANY = 3

    DELIVERY_CHOICES = (
        (DELIVERY_DISTRIBUTION_CENTER, _("Entrega en centro de distribución")),
        (DELIVERY_BRANCH_OFFICE, _("Entrega en sucursal")),
        (DELIVERY_ASSOCIATE_COMPANY, _("Entrega en empresa asociada")),
    )
