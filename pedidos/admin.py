from django.contrib import admin
from .models import Pedido, ItemPedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'criado', 'status', 'total')
    list_display_links = ('id', 'usuario')
    list_filter = ('status', 'criado')
    search_fields = ('usuario__username', 'id')
    ordering = ('-criado',)
    readonly_fields = ('total',)

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'produto', 'quantidade', 'subtotal')
    list_display_links = ('pedido', 'produto')
    search_fields = ('produto__nome', 'pedido__id')
    ordering = ('-pedido__criado',)
    readonly_fields = ('subtotal',)
