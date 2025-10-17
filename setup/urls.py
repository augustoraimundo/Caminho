from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from loja.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('loja.urls')),  # <- rotas da API
    path('', home),  # <- Rota raiz
    path('api/carrinho/', include('carrinho.urls')),
    path('api/auth/', include('conta.urls')),  # rotas de auth
    path('api/pedidos/', include('pedidos.urls')),
]

# servir arquivos de mídia (imagens) no ambiente de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)