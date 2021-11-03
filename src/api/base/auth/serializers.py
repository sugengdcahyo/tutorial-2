from rest_framework import (
    serializers
)
from django.contrib.auth.models import User
from django.db.models import Q


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active']


class LoginValidations(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class RegisterValidations(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, min_length=8)
    confirm_password = serializers.CharField(required=True, write_only=True)

    def validate_confirm_password(self, value):
        data = self.get_initial()
        if data.get('password') != value:
            raise serializers.ValidationError("confirm password not matching.")

    def validate(self, attrs):
        if User.objects.filter(
            Q(username=attrs['username']) |
            Q(email=attrs['email'])
        ):
            raise serializers.ValidationError(
                "registered username or email.")

        return attrs
