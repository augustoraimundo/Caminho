from rest_framework import viewsets
from .models import Produto
from .serializers import ProdutoSerializer
from django.http import HttpResponse
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


def home(request):
    return HttpResponse("<h1>🚀 API Wabel está rodando normalmente!</h1>")
