from django.urls import path

from pegawai import views

app_name = 'pegawai'
urlpatterns = [
    path('', views.index),
]
