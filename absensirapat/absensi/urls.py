from django.urls import path

from absensi import views

urlpatterns = [
    path('tambah-rapat/', views.tambah_rapat, name='tambahRapatUrl'),
    path('', views.index, name='indexUrl'),
]
