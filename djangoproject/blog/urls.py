from django.conf.urls import url
from django.views.generic import ListView
from .models import Artikel
from .views import index, ArtikelListView

urlpatterns = [
    url(r'^(?P<penulis>\w+)/(?P<page>\d+)$', ArtikelListView.as_view(), name='list'),
    # url(r'^$', ListView.as_view(model=Artikel), name = 'list'),
]
