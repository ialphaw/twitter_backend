from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models import fields
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_joined',
                    'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'date_joined',
                           'last_login',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
         ),
    )

admin.site.register(Account, AccountAdmin)
