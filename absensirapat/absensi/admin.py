from django.contrib import admin

# Register your models here.
from absensi.models import Rapat, Peserta


@admin.register(Rapat)
class RapatAdmin(admin.ModelAdmin):
    list_display = ('meeting_id', 'tanggal', 'agenda')
    ordering = ('tanggal',)


@admin.register(Peserta)
class PesertaAdmin(admin.ModelAdmin):
    list_display = ('rapat_id', 'nama', 'nip')
