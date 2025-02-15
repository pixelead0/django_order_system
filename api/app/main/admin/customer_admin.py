from django.contrib import admin
from app.main.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Admin for custmer catalog."""

    list_display = (
        "name",
        "code",
        "customer_type",
        "is_active",
        "updated_at",
    )

    search_fields = ("name",)

    ordering = ("name",)
    list_filter = ("customer_type",)
