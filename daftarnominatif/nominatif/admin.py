from django.contrib import admin

# Register your models here.
from .models import Golongan, Jabatan, Pegawai, Bagian


@admin.register(Bagian)
class BagianAdmin(admin.ModelAdmin):
    pass


@admin.register(Golongan)
class GolonganAdmin(admin.ModelAdmin):
    list_display = ('gol', 'pangkat',)


@admin.register(Jabatan)
class JabatanAdmin(admin.ModelAdmin):
    pass


@admin.register(Pegawai)
class PegawaiAdmin(admin.ModelAdmin):
    pass
