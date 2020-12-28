from django.urls import path

from . import views

app_name = 'peserta_app'
urlpatterns = [
    path('<str:rapat_id>', views.index, name='indexUrl'),
]
