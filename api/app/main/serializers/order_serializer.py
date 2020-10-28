from app.main.models import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    """Order Serializer."""

    # customer_type_name = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        exclude = (
            'is_active',
            'created_at',
            'updated_at',
        )
