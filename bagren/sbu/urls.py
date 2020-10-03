from django.urls import path
from sbu import views

app_name = 'sbu'
urlpatterns = [
    path('', views.index, name='index'),
]
