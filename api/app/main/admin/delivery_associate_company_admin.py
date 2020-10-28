from app.main.models import DeliveryAssociateCompany
from django.contrib import admin


@admin.register(DeliveryAssociateCompany)
class DeliveryAssociateCompanyAdmin(admin.ModelAdmin):
    """Admin for delivery associate company catalog."""

    list_display = (
        "name",
        "is_active",
        "updated_at",
    )

    search_fields = ("name",)

    ordering = ("name",)
