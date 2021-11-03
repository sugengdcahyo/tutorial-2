from django.views.generic import base
from rest_framework import routers
from api.base.auth.viewsets import (
    RegisterViewsets,
    LoginViewsets
)

router = routers.DefaultRouter()
router.register('auth/register', RegisterViewsets, basename='register-viewsets')
router.register('auth/login', LoginViewsets, basename='login-viewsets')
api_v1 = router.urls