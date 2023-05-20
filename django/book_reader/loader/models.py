from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.TextField(max_length=100)
    created = models.DateTimeField(default=timezone.now)
    content_file = models.FileField()
    description = models.TextField(max_length=1000, null=True, blank=True)
    stats = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.title}"
