from django.urls import path
from .views import UsuarioRegisterView, UsuarioLoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', UsuarioLoginView.as_view(), name='login'),
    path('register/', UsuarioRegisterView.as_view(), name='user-register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]