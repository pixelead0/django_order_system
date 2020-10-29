
# Django REST Framework
from rest_framework import generics

# Models
from app.main.models import Order

# Serializers
from app.main.serializers import OrderSerializer


class OrderListCreate(generics.ListCreateAPIView):
    """View para ver listar y crear las ordenes de un cliente."""
    queryset = Order.objects.actives()
    serializer_class = OrderSerializer


class OrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """Para ver el detalle, actualizar y eliminar la orden de un cliente."""

    queryset = Order.objects.actives()
    serializer_class = OrderSerializer
