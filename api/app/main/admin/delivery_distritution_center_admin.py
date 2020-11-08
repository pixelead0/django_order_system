from django.contrib import admin
from app.main.models import DeliveryDistributionCenter


@admin.register(DeliveryDistributionCenter)
class DeliveryDistributionCenterAdmin(admin.ModelAdmin):
    """Admin for delivery associate company catalog."""

    list_display = (
        "name",
        "is_active",
        "updated_at",
    )

    search_fields = ("name",)

    ordering = ("name",)
