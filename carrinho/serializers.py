from rest_framework import serializers
from .models import Carrinho, ItemCarrinho
from loja.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco']

class ItemCarrinhoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)
    produto_id = serializers.PrimaryKeyRelatedField(
        queryset=Produto.objects.all(), source='produto', write_only=True
    )

    class Meta:
        model = ItemCarrinho
        fields = ['id', 'produto', 'produto_id', 'quantidade']

class CarrinhoSerializer(serializers.ModelSerializer):
    itens = ItemCarrinhoSerializer(many=True)

    class Meta:
        model = Carrinho
        fields = ['id', 'usuario', 'itens']
        read_only_fields = ['usuario']