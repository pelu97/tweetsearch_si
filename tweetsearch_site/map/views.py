from django.shortcuts import render
import json
from django.core.serializers import serialize
from django.http import JsonResponse
from django import forms


from .models import TweetSpot, Query
from .load import delete, update




# Create your views here.


def index(request):
    return render(request, 'map/index.html')


def query(request, year, month, day):
    new_query = "%s_%s_%s" % (year, month, day)
    delete()
    update(new_query)

    return render(request, "map/query.html")
