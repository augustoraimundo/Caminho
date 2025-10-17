from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Pedido, ItemPedido
from carrinho.models import Carrinho, ItemCarrinho
from .serializers import PedidoSerializer

class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        usuario = request.user

        try:
            carrinho = Carrinho.objects.get(usuario=usuario)
        except Carrinho.DoesNotExist:
            return Response({'erro': 'Carrinho vazio.'}, status=status.HTTP_400_BAD_REQUEST)

        if not carrinho.itens.exists():
            return Response({'erro': 'Carrinho está vazio.'}, status=status.HTTP_400_BAD_REQUEST)

        # Criar o pedido
        pedido = Pedido.objects.create(usuario=usuario)

        for item in carrinho.itens.all():
            ItemPedido.objects.create(
                pedido=pedido,
                produto=item.produto,
                quantidade=item.quantidade
            )

        # Esvaziar o carrinho
        carrinho.itens.all().delete()

        serializer = PedidoSerializer(pedido)
        return Response(serializer.data, status=status.HTTP_201_CREATED)