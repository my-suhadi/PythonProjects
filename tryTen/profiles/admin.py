from django.contrib import admin

# Register your models here.
from .models import profile


class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = profile


admin.site.register(profile, ProfileAdmin)
