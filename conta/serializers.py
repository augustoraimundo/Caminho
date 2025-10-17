from django.contrib.auth.models import User
from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()

class UsuarioRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['nome', 'email', 'senha']

    def create(self, validated_data):
        usuario = User(
            email=validated_data['email'],
            username=validated_data['nome']
        )
        usuario.set_password(validated_data['senha'])
        usuario.save()
        return usuario

