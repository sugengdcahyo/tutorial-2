from rest_framework import (
    viewsets,
    generics,
    permissions,
    status
)
from rest_framework.decorators import permission_classes

class LoginViewsets(generics.CreateAPIView, viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = None

    def post(self, request, *args, **kwargs):
        # !type your code
        pass


class RegisterViewsets(generics.CreateAPIView, viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = None

    def post(self, request, *args, **kwargs):
        # !type your code
        pass