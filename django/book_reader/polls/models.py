from django.db import models

# Create your models here.


class Thing(models.Model):
    thing_name = models.TextField(max_length=50)

    def __str__(self):
        return self.thing_name
