from rest_framework import serializers
from .models import Pedido, ItemPedido
from loja.serializers import ProdutoSerializer

class ItemPedidoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = ItemPedido
        fields = ['id', 'produto', 'quantidade', 'subtotal']

class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True, read_only=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'usuario', 'criado', 'status', 'itens', 'total']
        read_only_fields = ['usuario', 'status', 'criado', 'total']