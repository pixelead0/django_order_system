from app.main.models import DeliveryBranchOffice
from django.contrib import admin


@admin.register(DeliveryBranchOffice)
class DeliveryBranchOfficeAdmin(admin.ModelAdmin):
    """Admin for delivery associate company catalog."""

    list_display = (
        "name",
        "is_active",
        "updated_at",
    )

    search_fields = ("name",)

    ordering = ("name",)
