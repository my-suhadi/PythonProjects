from django.contrib import admin

# Register your models here.
from .models import Peserta


@admin.register(Peserta)
class PesertaAdmin(admin.ModelAdmin):
    list_display = ('rapat_id', 'nama', 'nip')
