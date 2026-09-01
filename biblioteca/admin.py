from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    Usuario,
    Categoria,
    
)


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = (
        "id",
        "username",
        "nome",
        "cpf",
        "is_staff",
        "is_active",
    )

    search_fields = (
        "username",
        "nome",
        "cpf",
        "rg",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Dados pessoais",
            {
                "fields": (
                    "nome",
                    "rg",
                    "cpf",
                    "endereco",
                    "foto",
                    "descricao",
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Dados pessoais",
            {
                "fields": (
                    "nome",
                    "rg",
                    "cpf",
                    "endereco",
                    "foto",
                    "descricao",
                )
            },
        ),
    )



@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
    )

    search_fields = ("nome",)

