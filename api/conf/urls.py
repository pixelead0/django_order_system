from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# from rest_framework.schemas.coreapi import AutoSchema
# from rest_framework_swagger.views import get_swagger_view
# schema_view = get_swagger_view(title='User API')
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Dajngo Order System",
        default_version="v1",
        description="This project implements an order system",
        contact=openapi.Contact(email="adangq@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(
        "swagger(?P<format>\.json|\.yaml)",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),

    # path("api_doc/", schema_view),
    path("admin/", admin.site.urls),
    path("v1/", include("app.main.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
