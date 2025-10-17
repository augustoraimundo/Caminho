from rest_framework import generics
from .serializers import UsuarioRegisterSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()

class UsuarioRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioRegisterSerializer


class UsuarioRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioRegisterSerializer

class UsuarioLoginView(APIView):
    def post(self, request):
        nome = request.data.get("nome")
        senha = request.data.get("senha")
        usuario = authenticate(username=nome, password=senha)

        if usuario:
            token, _ = Token.objects.get_or_create(username=usuario)
            return Response({"token": token.key})
        return Response({"erro": "Credenciais inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
