from app.main.models import Article
from django.contrib import admin


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Admin for article catalog."""

    list_display = (
        "name",
        "is_active",
        "updated_at",
    )

    search_fields = ("name",)

    ordering = ("name",)
