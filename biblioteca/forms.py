from django import forms

from biblioteca.models import Autor, Autor, Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ("nome",)


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = (
            "nome",
            "biografia",
            "data_nascimento",
        )

        widgets = {
            "data_nascimento": forms.DateInput(
                attrs={"type": "date"}
            ),
        }