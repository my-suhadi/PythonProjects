from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^create/', views.create, name='create'),
	url(r'^delete/(?P<delete_id>[0-9]+)', views.hapus, name='hapus'),
	url(r'^update/(?P<update_id>[0-9]+)', views.ubah, name='ubah'),
	url(r'^$', views.list, name='list'),
]