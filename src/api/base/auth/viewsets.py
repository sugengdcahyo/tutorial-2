from django.contrib.auth.models import User
from rest_framework import (
    serializers,
    viewsets,
    generics,
    permissions,
    status
)
from rest_framework.response import Response
from api.base.auth.serializers import RegisterValidations
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
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(
            **serializer.data
        )

        return Response(request.data)