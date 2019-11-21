from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import TweetSpot

# Register your models here.


admin.site.register(TweetSpot, LeafletGeoAdmin)
