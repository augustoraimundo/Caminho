from django.urls import path
from .views import ItemCarrinhoListCreateView, ItemCarrinhoUpdateDeleteView

urlpatterns = [
    path('', ItemCarrinhoListCreateView.as_view(), name='carrinho-itens-list-create'),
    path('<int:item_id>/', ItemCarrinhoUpdateDeleteView.as_view(), name='carrinho-item-update-delete'),
]