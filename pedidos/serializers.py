from rest_framework import serializers
from .models import Pedido, ItemPedido
from loja.serializers import ProdutoSerializer  # reutilizável

class ItemPedidoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)

    class Meta:
        model = ItemPedido
        fields = ['id', 'produto', 'quantidade']

class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'usuario', 'criado', 'pago', 'itens']
        read_only_fields = ['usuario', 'pago']