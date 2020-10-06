from django.urls import path

from sbu import views

app_name = 'sbu'
urlpatterns = [
    path('', views.index, name='index'),
    path('hapus/<str:delete_id>', views.hapus_sbu, name='hapus'),
    path('tambah/', views.tambah_sbu, name='tambah'),
]
