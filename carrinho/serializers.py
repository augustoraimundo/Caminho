from rest_framework import serializers
from .models import ItemCarrinho
from loja.serializers import ProdutoSerializer

class ItemCarrinhoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)
    produto_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ItemCarrinho
        fields = ['id', 'produto', 'produto_id', 'quantidade']

    def validate_produto_id(self, value):
        from loja.models import Produto
        if not Produto.objects.filter(id=value).exists():
            raise serializers.ValidationError("Produto não existe.")
        return value

    def create(self, validated_data):
        carrinho = self.context['carrinho']
        produto_id = validated_data['produto_id']
        quantidade = validated_data.get('quantidade', 1)

        item, created = ItemCarrinho.objects.get_or_create(
            carrinho=carrinho,
            produto_id=produto_id,
            defaults={'quantidade': quantidade}
        )
        if not created:
            item.quantidade += quantidade
            item.save()
        return item