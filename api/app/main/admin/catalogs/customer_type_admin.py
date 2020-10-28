from app.main.models import CustomerType
from django.contrib import admin


@admin.register(CustomerType)
class CustomerTypeAdmin(admin.ModelAdmin):
    """Admin for customer type catalog."""

    list_display = (
        "name",
        "is_active",
        "updated_at",
    )

    search_fields = ("name",)

    ordering = ("name",)
