from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca', 'categoria', 'preco', 'criado')
