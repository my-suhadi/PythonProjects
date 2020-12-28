from django.contrib import admin

# Register your models here.
from .models import Rapat


@admin.register(Rapat)
class RapatAdmin(admin.ModelAdmin):
    list_display = ('meeting_id', 'tanggal', 'agenda')
    ordering = ('tanggal',)
