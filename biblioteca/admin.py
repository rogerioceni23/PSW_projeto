from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

admin.site.site_header = "Administração da Biblioteca Digital"
admin.site.site_title = "Biblioteca Digital"
admin.site.index_title = "Gerenciamento da biblioteca"

from .models import (
    Usuario,
    Autor,
    Categoria,
    Livro,
    UsuarioLivro,
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


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "data_nascimento",
    )

    search_fields = ("nome",)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
    )

    search_fields = ("nome",)


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "titulo",
        "ano_publicacao",
    )

    search_fields = (
        "titulo",
        "descricao",
    )

    list_filter = ("ano_publicacao",)

    filter_horizontal = (
        "autores",
        "categorias",
    )


@admin.register(UsuarioLivro)
class UsuarioLivroAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "usuario",
        "livro",
        "data_hora",
    )

    search_fields = (
        "usuario__nome",
        "usuario__username",
        "livro__titulo",
    )

    list_filter = ("data_hora",)