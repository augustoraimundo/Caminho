from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Usuario

class UsuarioAdmin(BaseUserAdmin):
    model = Usuario
    list_display = ['username', 'primeiro_nome', 'ultimo_nome', 'telefone', 'endereco', 'is_staff', 'is_active']
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('primeiro_nome', 'ultimo_nome', 'telefone', 'endereco')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('primeiro_nome', 'ultimo_nome', 'telefone', 'endereco')}),
    )

admin.site.register(Usuario, UsuarioAdmin)
