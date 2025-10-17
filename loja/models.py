from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=45)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    criado = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to= 'produtos/', blank=True, null=True)
    marca = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50,default='Geral')

    def __str__(self):
        return self.nome