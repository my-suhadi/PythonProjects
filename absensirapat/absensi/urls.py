from django.urls import path, include

from absensi import views

urlpatterns = [
    path('', views.index, name='indexUrl'),
    path('tambah-rapat/', views.tambah_rapat, name='tambahRapatUrl'),
    path('ubah-rapat/<str:rapat_id>', views.ubah_rapat, name='ubahRapatUrl'),
    path('hapus-rapat/<str:rapat_id>', views.hapus_rapat, name='hapusRapatUrl'),
]
