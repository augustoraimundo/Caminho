from django.contrib import admin
from .models import Carrinho, ItemCarrinho

@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario')
    search_fields = ('usuario__username',)

@admin.register(ItemCarrinho)
class ItemCarrinhoAdmin(admin.ModelAdmin):
    list_display = ('carrinho', 'produto', 'quantidade')
    list_filter = ('produto',)
    search_fields = ('produto__nome', 'carrinho__usuario__username')
