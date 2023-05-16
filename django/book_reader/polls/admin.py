from django.contrib import admin

# Register your models here.
from .models import Thing, Book

admin.site.register(Thing)
admin.site.register(Book)
