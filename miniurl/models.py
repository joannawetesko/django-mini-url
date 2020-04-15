from django.db import models


class URL(models.Model):
    url = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True)
