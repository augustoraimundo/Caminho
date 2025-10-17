from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Carrinho, ItemCarrinho
from .serializers import CarrinhoSerializer, ItemCarrinhoSerializer
from django.shortcuts import get_object_or_404

class CarrinhoViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
        serializer = CarrinhoSerializer(carrinho)
        return Response(serializer.data)

    def add_item(self, request):
        carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
        serializer = ItemCarrinhoSerializer(data=request.data)
        if serializer.is_valid():
            item = serializer.save(carrinho=carrinho)
            return Response(ItemCarrinhoSerializer(item).data, status=201)
        return Response(serializer.errors, status=400)

    def remove_item(self, request, pk=None):
        carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
        item = get_object_or_404(ItemCarrinho, pk=pk, carrinho=carrinho)
        item.delete()
        return Response(status=204)
