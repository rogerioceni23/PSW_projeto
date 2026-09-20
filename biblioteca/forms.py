from django import forms

from .models import Categoria, Livro


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