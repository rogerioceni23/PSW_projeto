from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Autor, Categoria, Livro, Usuario, UsuarioLivro


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nome"]


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = [
            "titulo",
            "descricao",
            "ano_publicacao",
            "capa",
            "arquivo_pdf",
            "categorias",
            "autores",
        ]


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = [
            "nome",
            "biografia",
            "data_nascimento",
        ]


class UsuarioLivroForm(forms.ModelForm):
    class Meta:
        model = UsuarioLivro
        fields = [
            "usuario",
            "livro",
            "data_hora",
        ]
        widgets = {
            "data_hora": forms.DateTimeInput(
                attrs={"type": "datetime-local"}
            ),
        }


class UsuarioCriacaoForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            "username",
            "nome",
            "rg",
            "cpf",
            "endereco",
            "foto",
            "descricao",
            "groups",
        ]


class UsuarioEdicaoForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            "username",
            "nome",
            "rg",
            "cpf",
            "endereco",
            "foto",
            "descricao",
            "groups",
            "is_active",
        ]