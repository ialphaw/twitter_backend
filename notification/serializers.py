from rest_framework import serializers

from .models import Notif


class NotifSerializer(serializers.ModelSerializer):
    def liker_username(self, obj):
        try:
            return obj.liker.username
        except:
            return None

    def follower_username(self, obj):
        try:
            return obj.follower.username
        except:
            return None

    def post_body(self, obj):
        try:
            return obj.post.body[:10]
        except:
            return None

    liker_username_ = serializers.SerializerMethodField('liker_username')
    follower_username_ = serializers.SerializerMethodField('follower_username')
    post_body_ = serializers.SerializerMethodField('post_body')

    class Meta:
        model = Notif
        fields = ('is_like', 'liker_username_', 'post_body_',
                  'is_follow', 'follower_username_', 'is_read')
