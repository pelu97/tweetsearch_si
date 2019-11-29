from django.shortcuts import render
import json
from django.core.serializers import serialize
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse


from .models import TweetSpot, Query
from .load import init, delete, update
from .forms import QueryConfig




# Create your views here.


def index(request):

    if(request.method == 'POST'):
        form = QueryConfig(request.POST)

        if(form.is_valid()):
            init()
            date = form.cleaned_data['date']
            est_mun = form.cleaned_data['est_mun']
            return HttpResponseRedirect(reverse("query", args=[date.year, date.month, date.day]))

    else:
        form = QueryConfig()
        context = {
            'form': form,
        }

        return render(request, 'map/index.html', context)
    # return render(request, 'map/index.html')


def query(request, year, month, day):
    new_query = "%s-%s-%s" % (year, month, day)
    delete()
    update(new_query)

    return render(request, "map/query.html")
