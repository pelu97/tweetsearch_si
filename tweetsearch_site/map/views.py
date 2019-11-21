from django.shortcuts import render

from .models import TweetSpot

# Create your views here.


def index(request):
    map = TweetSpot.objects.order_by()
    return HttpResponse("Hello world. You're at the maps index.")
