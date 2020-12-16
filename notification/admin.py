from django.contrib import admin

from .models import Notif

class FollowNotifAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_like', 'is_follow', 'is_read')


admin.site.register(Notif, FollowNotifAdmin)
