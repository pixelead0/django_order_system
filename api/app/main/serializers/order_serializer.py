from app.main.models import Order, OrderDetail
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    """Order Serializer."""

    class Meta:
        model = Order
        # fields = ["order_details"]
        exclude = (
            "is_active",
            "created_at",
            "updated_at",
        )
