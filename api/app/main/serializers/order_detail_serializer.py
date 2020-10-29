from app.main.models import Order, OrderDetail
from rest_framework import serializers


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        exclude = (
            "order",
            "is_active",
            "created_at",
            "updated_at",
        )
