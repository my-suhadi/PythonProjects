from django.urls import path

from . import views

app_name = 'pesertaApp'
urlpatterns = [
    path('<str:rapat_id>', views.index, name='indexUrl'),
    path('export/<str:rapat_id>/', views.export_peserta, name='exportPesertaUrl'),
    path('get_data_peserta/', views.get_data_peserta, name='getDataPesertaUrl'),
]
