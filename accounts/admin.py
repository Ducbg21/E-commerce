from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'phone_number', 'date_joined', 'last_login', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')

    ordering = ('date_joined',)
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    filter_horizontal = ()
    fieldsets = ()
admin.site.register(Account, AccountAdmin)