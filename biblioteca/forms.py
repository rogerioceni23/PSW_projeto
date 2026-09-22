from django import forms
from django.contrib.auth.forms import (
    PasswordChangeForm,
    UserCreationForm,
)

from .models import (
    Autor,
    Categoria,
    Livro,
    Usuario,
    UsuarioLivro,
)


class FormularioTablerMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for campo in self.fields.values():
            if isinstance(
                campo.widget,
                (forms.Select, forms.SelectMultiple),
            ):
                campo.widget.attrs["class"] = "form-select"

            elif isinstance(
                campo.widget,
                forms.CheckboxInput,
            ):
                campo.widget.attrs["class"] = "form-check-input"

            else:
                campo.widget.attrs["class"] = "form-control"


class CategoriaForm(
    FormularioTablerMixin,
    forms.ModelForm,
):
    class Meta:
        model = Categoria
        fields = [
            "nome",
        ]


class LivroForm(
    FormularioTablerMixin,
    forms.ModelForm,
):
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
        widgets = {
            "descricao": forms.Textarea(
                attrs={"rows": 4}
            ),
        }


class AutorForm(
    FormularioTablerMixin,
    forms.ModelForm,
):
    class Meta:
        model = Autor
        fields = [
            "nome",
            "biografia",
            "data_nascimento",
        ]
        widgets = {
            "biografia": forms.Textarea(
                attrs={"rows": 4}
            ),
            "data_nascimento": forms.DateInput(
                attrs={"type": "date"}
            ),
        }


class UsuarioLivroForm(
    FormularioTablerMixin,
    forms.ModelForm,
):
    class Meta:
        model = UsuarioLivro
        fields = [
            "usuario",
            "livro",
            "data_hora",
        ]
        widgets = {
            "data_hora": forms.DateTimeInput(
                attrs={"type": "datetime-local"},
                format="%Y-%m-%dT%H:%M",
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["data_hora"].input_formats = [
            "%Y-%m-%dT%H:%M",
        ]


class UsuarioCriacaoForm(
    FormularioTablerMixin,
    UserCreationForm,
):
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
        widgets = {
            "descricao": forms.Textarea(
                attrs={"rows": 4}
            ),
        }


class UsuarioEdicaoForm(
    FormularioTablerMixin,
    forms.ModelForm,
):
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
        widgets = {
            "descricao": forms.Textarea(
                attrs={"rows": 4}
            ),
        }


class CadastroLeitorForm(
    FormularioTablerMixin,
    UserCreationForm,
):
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
        ]
        widgets = {
            "descricao": forms.Textarea(
                attrs={"rows": 4}
            ),
        }


class PerfilUsuarioForm(
    FormularioTablerMixin,
    forms.ModelForm,
):
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
        ]
        widgets = {
            "descricao": forms.Textarea(
                attrs={"rows": 4}
            ),
        }


class AlterarSenhaForm(
    FormularioTablerMixin,
    PasswordChangeForm,
):
    pass