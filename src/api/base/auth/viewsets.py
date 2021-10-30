from api.base.auth.serializers import RegisterValidations, UserSerializer
from django.contrib.auth.models import User
from rest_framework import (
    serializers,
    viewsets,
    generics,
    permissions,
    status
)
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.db import transaction
class LoginViewsets(generics.CreateAPIView, viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = None

    def post(self, request, *args, **kwargs):
        # !type your code
        pass


class RegisterViewsets(generics.CreateAPIView, viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterValidations

    def create(self, request, *args, **kwargs):
        # !type your code
        validation = self.serializer_class(data=request.data)
        validation.is_valid(raise_exception=True)
        with transaction.atomic():
            user = User.objects.create_user(
                **validation.data
            )
            token, created = Token.objects.get_or_create(user=user)

        serializer = UserSerializer(user, many=False)
        response = {
            "token": token.key,
            "user": serializer.data
        }

        return Response(response)