from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<str:task_id>/', views.update_task, name='update'),
    path('delete/<str:task_id>/', views.delete_task, name='delete'),
]
