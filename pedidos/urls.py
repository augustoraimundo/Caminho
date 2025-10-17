from django.urls import path
from .views import PedidoListView, PedidoDetailView, CheckoutView, MarcarPagoView

urlpatterns = [
    path('', PedidoListView.as_view(), name='pedidos-list'),
    path('<int:pk>/', PedidoDetailView.as_view(), name='pedido-detail'),
    path('checkout/', CheckoutView.as_view(), name='pedido-checkout'),
    path('<int:pk>/pagar/', MarcarPagoView.as_view(), name='pedido-marcar-pago'),
]