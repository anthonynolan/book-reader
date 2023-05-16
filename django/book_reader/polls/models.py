from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Thing(models.Model):
    thing_name = models.TextField(max_length=50)
    created = models.DateTimeField(default=timezone.now)

    def was_published_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return f"{self.id}, {self.thing_name}, {self.created}"


class Book(models.Model):
    title = models.TextField(max_length=100)
    created = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return f"{self.title}"
