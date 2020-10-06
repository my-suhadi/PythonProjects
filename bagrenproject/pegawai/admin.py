from django.contrib import admin

# Register your models here.
from .models import Pangkat


class PangkatAdmin(admin.ModelAdmin):
    readonly_fields = [
        'pangkat_id',
    ]


admin.site.register(Pangkat)
