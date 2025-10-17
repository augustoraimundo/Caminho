from django.contrib import admin
from .models import Carrinho, ItemCarrinho

class ItemCarrinhoInline(admin.TabularInline):
    model = ItemCarrinho
    extra = 1

@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    inlines = [ItemCarrinhoInline]
