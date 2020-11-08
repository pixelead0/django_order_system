from django.db import models


class ManagerTimestampMixin(models.Manager):
    """Provides additional filtering."""

    def actives(self):
        """Return records with an `is_active` flag set as `True`."""
        return super().get_queryset().filter(is_active=True)

    def inactives(self):
        """Return records with an `is_active` flag set as `False`."""
        return super().get_queryset().filter(is_active=False)
