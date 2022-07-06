from pydoc_data.topics import topics
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from app.models import *

def display_topic(request):
    LOT=Topic.objects.all()
    LOW=Webpage.objects.all()
    d={'topics':LOT,'webpages':LOW}
    return render(request,'display_topic.html',d)