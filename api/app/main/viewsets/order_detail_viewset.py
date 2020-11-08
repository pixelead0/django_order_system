# Django REST Framework
from rest_framework import generics

# Models
from app.main.models import OrderDetail

# Serializers
from app.main.serializers import OrderDetailSerializer


class OrderDetailListCreate(generics.ListCreateAPIView):
    """View para ver listar y crear las ordenes de un cliente."""

    queryset = OrderDetail.objects.actives()
    serializer_class = OrderDetailSerializer


class OrderDetailRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """Para ver el detalle, actualizar y eliminar la orden de un cliente."""

    queryset = OrderDetail.objects.actives()
    serializer_class = OrderDetailSerializer
