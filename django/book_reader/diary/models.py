from django.db import models

from django.utils import timezone


# Create your models here.
class DiaryEntry(models.Model):
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=2000, null=True, blank=True)
