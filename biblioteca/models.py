from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Usuario(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    biografia = models.TextField()
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ano_publicacao = models.PositiveIntegerField()

    autores = models.ManyToManyField(
        Autor,
        related_name="livros"
    )

    categorias = models.ManyToManyField(
        Categoria,
        related_name="livros"
    )

    capa = models.ImageField(
        upload_to="capas/",
        blank=True,
        null=True
    )

    arquivo_pdf = models.FileField(
        upload_to="pdfs/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.titulo


class Avaliacao(models.Model):
    livro = models.ForeignKey(
        Livro,
        on_delete=models.CASCADE,
        related_name="avaliacoes"
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="avaliacoes"
    )

    nota = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    comentario = models.TextField()

    data_criacao = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-data_criacao"]

    def __str__(self):
        return (
            f"{self.usuario.username} - "
            f"{self.livro.titulo}"
        )


class Perfil(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name="perfil"
    )

    foto = models.ImageField(
        upload_to="perfis/",
        blank=True,
        null=True
    )

    descricao = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"Perfil de {self.usuario.username}"