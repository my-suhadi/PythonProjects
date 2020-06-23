from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from akun.models import Akun


class AdminAkun(UserAdmin):
    # overide paramter2 berikut ini utk kustom tampilan admin
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Akun, AdminAkun)
