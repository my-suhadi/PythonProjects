from django.conf.urls import url

from .views import artikelIndexView, artikelAddView, artikelAddView2

urlpatterns = [
    url(r'^add2/$', artikelAddView2, name='tambah2'),
    url(r'^add/$', artikelAddView, name='tambah'),
    url(r'^$', artikelIndexView, name='index'),
]