from rest_framework import serializers

from .models import Notif

class NotifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notif
        fields = ('is_like', 'liker', 'post', 'is_follow', 'follower', 'following', 'is_read', 'when')
