from rest_framework import serializers
from app.main.models import Order


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
