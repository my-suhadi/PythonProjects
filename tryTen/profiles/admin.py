from django.contrib import admin

# Register your models here.
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = Profile


admin.site.register(Profile, ProfileAdmin)
