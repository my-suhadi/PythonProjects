from django.urls import path
from usulan import views

app_name = 'usulan'
urlpatterns = [
    path('', views.index, name='index'),
]