from django.db import models
from django.utils import timezone
from django.conf import settings


class URL(models.Model):
    url = models.URLField()
    date_created = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False
    )
    url_expires = models.DateTimeField(
        blank=False,
        null=False,
        default=timezone.now() + timezone.timedelta(days=settings.EXPIRATION_DAYS)
    )

    def is_valid(self):
        return timezone.now() < self.url_expires
