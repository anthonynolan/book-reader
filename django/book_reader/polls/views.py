from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Thing

# Create your views here.


def index(request):
    thing = Thing(thing_name="anthony")
    thing.save()

    return HttpResponse(f"hello {thing.id}")


def add(request):
    return HttpResponse("add char called")
