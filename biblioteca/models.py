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

class Autor(models.Model):
    nome = models.CharField(max_length=200)
    biografia = models.TextField()
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ano_publicacao = models.IntegerField()
    capa = models.ImageField(upload_to="capas/")
    arquivo_pdf = models.FileField(upload_to="pdfs/")

    categorias = models.ManyToManyField(
        Categoria,
        related_name="livros",
        db_table="livro_categoria",
    )

    autores = models.ManyToManyField(
        Autor,
        related_name="livros",
        db_table="autor_livro",
    )

    def __str__(self):
        return self.titulo


class UsuarioLivro(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="associacoes_livros",
    )

    livro = models.ForeignKey(
        Livro,
        on_delete=models.CASCADE,
        related_name="associacoes_usuarios",
    )

    data_hora = models.DateTimeField()

    class Meta:
        db_table = "usuario_livro"

    def __str__(self):
        return f"{self.usuario} — {self.livro}"