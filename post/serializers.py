from rest_framework import serializers

from .models import Post, Like


class PostHashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'body', 'image', 'video')


class PostSerializer(serializers.ModelSerializer):
    def get_username(self, obj):
        return obj.author.username

    def get_retweet_username_from(self, obj):
        try:
            return obj.retweeted_from.username
        except:
            return None

    def get_retweet_username_by(self, obj):
        try:
            return obj.retweeted_by.username
        except:
            return None

    username = serializers.SerializerMethodField('get_username')
    retweeted_from = serializers.SerializerMethodField('get_retweet_username_from')
    retweeted_by = serializers.SerializerMethodField('get_retweet_username_by')

    class Meta:
        model = Post
        fields = ('id', 'username', 'body', 'image', 'video', 'retweeted_from', 'retweeted_by')


class RetweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id',)


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('post',)
