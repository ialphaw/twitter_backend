from django.contrib import admin

from .models import Post, Hashtag, Like

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'short_body', 'is_retweeted', 'retweeted_from', 'created_time')


class HashtagAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Hashtag, HashtagAdmin)
admin.site.register(Like)
