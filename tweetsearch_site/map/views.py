from django.shortcuts import render
import json
from django.core.serializers import serialize
from django.http import JsonResponse


from .models import TweetSpot
from .load import delete, update

# Create your views here.
def index(request):
    # print("Running update")
    update()
    return render(request, 'map/index.html')
