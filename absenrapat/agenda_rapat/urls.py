from django.urls import path

from agenda_rapat import views

urlpatterns = [
    path('', views.index, name='indexUrl'),
]