from django.conf.urls import url
from .models import Artikel
from .views import ArtikelListView, ArtikelDetailView, ArtikelFormView

urlpatterns = [
    url(r'^create/$', ArtikelFormView.as_view(), name='create'),
    url(r'^(?P<penulis>\w+)/(?P<page>\d+)$', ArtikelListView.as_view(), name='list'),
    url(r'^(?P<penulis>\w+)/$', ArtikelListView.as_view(), name='list'),
    url(r'^detail/(?P<slug>[\w-]+)$', ArtikelDetailView.as_view(model=Artikel), name='detail'),
]
