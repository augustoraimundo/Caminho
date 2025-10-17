from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pedido, ItemPedido
from .serializers import PedidoSerializer
from carrinho.models import Carrinho
from django.shortcuts import get_object_or_404

class PedidoListView(generics.ListAPIView):
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Pedido.objects.filter(usuario=self.request.user).order_by('-criado')

class PedidoDetailView(generics.RetrieveAPIView):
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Pedido.objects.filter(usuario=self.request.user)

class CheckoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        usuario = request.user

        try:
            carrinho = Carrinho.objects.get(usuario=usuario)
        except Carrinho.DoesNotExist:
            return Response({'erro': 'Carrinho vazio.'}, status=status.HTTP_400_BAD_REQUEST)

        if not carrinho.itens.exists():
            return Response({'erro': 'Carrinho está vazio.'}, status=status.HTTP_400_BAD_REQUEST)

        # Verificar estoque
        for item in carrinho.itens.all():
            if item.quantidade > item.produto.estoque:
                return Response({
                    'erro': f"Produto '{item.produto.nome}' não possui estoque suficiente."
                }, status=status.HTTP_400_BAD_REQUEST)

        # Criar pedido
        pedido = Pedido.objects.create(usuario=usuario)

        # Criar itens do pedido e reduzir estoque
        for item in carrinho.itens.all():
            ItemPedido.objects.create(
                pedido=pedido,
                produto=item.produto,
                quantidade=item.quantidade
            )
            item.produto.estoque -= item.quantidade
            item.produto.save()

        # Esvaziar o carrinho
        carrinho.itens.all().delete()

        serializer = PedidoSerializer(pedido)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MarcarPagoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        pedido = get_object_or_404(Pedido, pk=pk, usuario=request.user)

        if pedido.status == 'PAGO':
            return Response({'detail': 'Pedido já está pago.'}, status=status.HTTP_400_BAD_REQUEST)

        pedido.status = 'PAGO'
        pedido.save()

        serializer = PedidoSerializer(pedido)
        return Response(serializer.data)