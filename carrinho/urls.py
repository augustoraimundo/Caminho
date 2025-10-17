from django.urls import path
from .views import CarrinhoViewSet

carrinho_view = CarrinhoViewSet.as_view({
    'get': 'list',
    'post': 'add_item'
})

urlpatterns = [
    path('', carrinho_view, name='ver-carrinho'),
    path('remover/<int:pk>/', CarrinhoViewSet.as_view({'delete': 'remove_item'}), name='remover-item'),]