from django.shortcuts import render
import json
from django.core.serializers import serialize
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse


from .models import TweetSpot, Query
from .load import delete, update, setkey
from .forms import QueryConfig, KeyConfig




# Create your views here.


def index(request):

    if(request.method == 'POST'):
        form = QueryConfig(request.POST)

        if(form.is_valid()):
            dateini = form.cleaned_data['dateini']
            datefim = form.cleaned_data['datefim']
            est_mun = form.cleaned_data['est_mun']
            keyword = form.cleaned_data['keyword']
            return HttpResponseRedirect(reverse("query", args=[dateini.year, dateini.month, dateini.day, datefim.year, datefim.month, datefim.day, keyword]))

    else:
        form = QueryConfig()
        context = {
            'form': form,
        }

        return render(request, 'map/index.html', context)
    # return render(request, 'map/index.html')


def keyconfig(request):
    if(request.method == 'POST'):
        form = KeyConfig(request.POST)

        if(form.is_valid()):
            keyword = form.cleaned_data['keyword']
            setkey(keyword)
            return HttpResponseRedirect(reverse("home", args=[]))

    else:
        form = KeyConfig()
        context = {
            'form': form,
        }

        return render(request, 'map/config.html', context)


def query(request, yearini, monthini, dayini, yearfim, monthfim, dayfim, keyword):
    if(dayini < 10):
        new_query_ini = "%s-%s-0%s" % (yearini, monthini, dayini)
    else:
        new_query_ini = "%s-%s-%s" % (yearini, monthini, dayini)
    if(dayfim < 10):
        new_query_fim = "%s-%s-0%s" % (yearfim, monthfim, dayfim)
    else:
        new_query_fim = "%s-%s-%s" % (yearfim, monthfim, dayfim)

    delete()
    update(new_query_ini, new_query_fim, keyword)

    return render(request, "map/query.html")
