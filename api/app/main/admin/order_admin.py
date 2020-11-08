from django.contrib import admin
from app.main.models import Order, OrderDetail


class OrderDetailInline(admin.TabularInline):
    """Order articles detail."""

    model = OrderDetail
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Admin for delivery associate company catalog."""

    list_display = (
        "number",
        "is_delivered",
        "customer",
        "delivery_type",
        "is_active",
        "updated_at",
    )

    search_fields = ("number",)
    ordering = ("number",)

    inlines = [
        OrderDetailInline,
    ]
