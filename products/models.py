from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_length=10, max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome