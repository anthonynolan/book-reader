from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Thing
from django.template import loader
from django.shortcuts import render, get_object_or_404

# Create your views here.


def index(request):
    latest_thing_list = Thing.objects.all()
    context = {"latest_thing_list": latest_thing_list}
    return render(request, "polls/index.html", context)


def detail(request, thing_id):
    thing = get_object_or_404(Thing, pk=thing_id)
    return render(request, "polls/detail.html", {"thing": thing})
