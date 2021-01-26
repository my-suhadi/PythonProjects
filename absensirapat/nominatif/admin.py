from django.contrib import admin

# Register your models here.
from .models import Bagian, Golongan, Jabatan, Pegawai


@admin.register(Bagian)
class BagianAdmin(admin.ModelAdmin):
    list_display = ('nama',)


@admin.register(Golongan)
class GolonganAdmin(admin.ModelAdmin):
    list_display = ('gol', 'pangkat',)


@admin.register(Jabatan)
class JabatanAdmin(admin.ModelAdmin):
    list_display = ('nama',)


@admin.register(Pegawai)
class PegawaiAdmin(admin.ModelAdmin):
    list_display = ('nama', 'nip', 'bagian',)
