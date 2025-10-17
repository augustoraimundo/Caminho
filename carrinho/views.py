from rest_framework import generics, permissions
from .models import Carrinho, ItemCarrinho
from .serializers import ItemCarrinhoSerializer

class CarrinhoMixin:
    def get_carrinho(self):
        carrinho, created = Carrinho.objects.get_or_create(usuario=self.request.user)
        return carrinho

class ItemCarrinhoListCreateView(CarrinhoMixin, generics.ListCreateAPIView):
    serializer_class = ItemCarrinhoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        carrinho = self.get_carrinho()
        return carrinho.itens.all()

    def perform_create(self, serializer):
        carrinho = self.get_carrinho()
        serializer.context['carrinho'] = carrinho
        serializer.save()

class ItemCarrinhoUpdateDeleteView(CarrinhoMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemCarrinhoSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = 'item_id'

    def get_queryset(self):
        carrinho = self.get_carrinho()
        return carrinho.itens.all()