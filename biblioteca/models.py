from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)
    endereco = models.CharField(max_length=255)
    foto = models.ImageField(upload_to="fotos/")
    descricao = models.TextField()

    livros = models.ManyToManyField(
        "Livro",
        through="UsuarioLivro",
        related_name="usuarios",
    )

    def __str__(self):
        return self.nome or self.username

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

