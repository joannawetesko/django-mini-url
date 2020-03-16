from django.db import models
from django.conf import settings
from django.utils import timezone

class URL(models.Model):
    url = models.URLField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_expired = models.DateTimeField(null=True, blank=True)
    hits = models.IntegerField(default=0)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def is_active(self):
        return timezone.now() < self.date_expired

    def __str__(self):
        return f"{self.user} - {self.url}"