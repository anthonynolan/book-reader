from django.db import models

# Create your models here.


class Thing(models.Model):
    thing_name = models.TextField(max_length=50)
