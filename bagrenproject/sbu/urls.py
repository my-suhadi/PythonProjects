from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^hapus/(?P<delete_id>[0-9]+)', views.hapus_sbu, name='hapus'),
	url(r'^tambah/', views.tambah_sbu, name='tambah'),
	url(r'^$', views.index, name='index'),
]