from rest_framework import serializers

from .models import Post


class PostHashtagSerializer(serializers.ModelSerializer):
    hashtag = serializers.CharField(max_length=64)

    class Meta:
        model = Post
        fields = ('id', 'body', 'hashtag')


class PostSerializer(serializers.ModelSerializer):
    def get_username(self, obj):
        return obj.author.username

    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Post
        fields = ('id', 'username', 'body')
