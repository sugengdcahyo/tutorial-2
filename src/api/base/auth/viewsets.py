from api.base.auth.serializers import (
    RegisterValidations, 
    UserSerializer,
    LoginValidations
)
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
from django.contrib.auth import authenticate
class LoginViewsets(generics.CreateAPIView, viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # !type your code
        '''
        - get params
        - validasi -> username | password
        - if username | email is exist -> next -> obj(user)
        - user.check_login(password)
          - authenticated ? response else error

        '''
        validation = LoginValidations(data=request.data)
        validation.is_valid(raise_exception=True)
        user = User.objects.filter(username=request.data['username'])
        if user:
            # user is exists.
            if not user[0].is_active:
                return Response({'message': 'your account is not activated'})
            if authenticate(**request.data):
                user_serializer = UserSerializer(user[0], many=False, context={'request': request})
                return Response(user_serializer.data, status=status.HTTP_200_OK)
        
        return Response({"message": "user not found."}, status=status.HTTP_401_UNAUTHORIZED)



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