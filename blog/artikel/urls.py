from django.conf.urls import url

from artikel.views import ArtikelListView, ArtikelDetailView, ArtikelKategoriListView

urlpatterns = [
    url(r'^kategori/(?P<kategori>[\w]+)/(?P<page>\d+)$', ArtikelKategoriListView.as_view(), name='kategori'),
    url(r'^detail/(?P<slug>[\w-]+)$', ArtikelDetailView.as_view(), name='detail'),  # nama parameter tdk boleh diganti
    url(r'^(?P<page>\d+)$', ArtikelListView.as_view(), name='list'),    # nama parameter tdk boleh diganti
]