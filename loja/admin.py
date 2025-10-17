from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'marca', 'categoria')
    list_display_links = ('id', 'nome')
    list_filter = ('marca', 'categoria')
    search_fields = ('nome', 'descricao', 'marca', 'categoria')
    ordering = ('nome',)
