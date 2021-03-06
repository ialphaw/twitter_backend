from rest_framework import serializers

from .models import Profile, Relation


class ProfileSerializer(serializers.ModelSerializer):

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email

    username = serializers.SerializerMethodField('get_username')
    email = serializers.SerializerMethodField('get_email')

    class Meta:
        model = Profile
        fields = ('username', 'email', 'bio', 'age', 'phone')


class RelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relation
        fields = ('to_user',)
