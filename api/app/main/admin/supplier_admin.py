from app.main.models import Supplier
from django.contrib import admin


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Admin for supplier catalog."""

    list_display = (
        "name",
        "is_active",
        "updated_at",
    )

    search_fields = ("name",)

    ordering = ("name",)
