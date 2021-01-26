from django.urls import path

from . import views

app_name = 'nominatifApp'
urlpatterns = [
    path('', views.index, name='indexUrl'),
    path('upload/', views.import_sheet, name='uploadUrl'),
]