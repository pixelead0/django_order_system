from rest_framework import serializers
from app.main.models import OrderDetail


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        exclude = (
            "order",
            "is_active",
            "created_at",
            "updated_at",
        )
