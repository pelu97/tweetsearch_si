# from django.urls import path

from django.conf import settings
from django.urls import path
from django.urls import re_path
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView

from .models import TweetSpot

# from . import views

urlpatterns = [
    # path('', views.index, name = 'index'),
    # url(r'admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name = 'map/index.html'), name = 'home'),
    # path('', GeoJSONLayerView.as_view(model = TweetSpot, properties = ('title', 'description')), name = 'data'),
    url(r'data.geojson$', GeoJSONLayerView.as_view(model = TweetSpot, properties = ('title', 'description')), name = 'data'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
