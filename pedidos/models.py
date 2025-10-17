from django.db import models
from django.conf import settings
from loja.models import Produto  # se você tem o app loja e modelo Produto

class Pedido(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return f"Pedido #{self.id} - {self.user.username}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"
