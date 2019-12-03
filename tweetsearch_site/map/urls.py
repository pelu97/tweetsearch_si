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
from . import views

# from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    # path('', views.QueryListView.as_view(), name = "query_select"),
    # path('<int:year>/<int:month>/<int:day>', views.query, name = "query"),
    path('<int:yearini>_<int:monthini>_<int:dayini>/<int:yearfim>_<int:monthfim>_<int:dayfim>', views.query, name = "query"),
    # url(r'admin/', admin.site.urls),
    # url(r'^$', TemplateView.as_view(template_name = 'map/index.html'), name = 'home'),
    url(r'data.geojson$', GeoJSONLayerView.as_view(model = TweetSpot, properties = ('title', 'qt_tweets', 'coe_sent', 'desc_qt', 'desc_coe')), name = 'data'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
