from django.contrib import admin

from .models import Post, Hashtag

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'short_body', 'created_time')


class HashtagAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Hashtag, HashtagAdmin)
