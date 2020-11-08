from django.urls import path
from rest_framework.routers import DefaultRouter

# Views
from app.main import viewsets

urlpatterns = [
    path("order", viewsets.OrderListCreate.as_view()),
    path("order/<pk>", viewsets.OrderRetrieveUpdateDestroy.as_view()),
    path("order_detail", viewsets.OrderDetailListCreate.as_view()),
    path("order_detail/<pk>", viewsets.OrderDetailRetrieveUpdateDestroy.as_view()),
]
