from rest_framework import serializers

from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=50)

    class Meta:
        model = Account
        fields = ('email', 'username', 'password', 'confirm_password')

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError('confirm password does not match')

        return data
