from django.contrib import admin

from .models import (
    Usuario,
    Autor,
    Categoria,
    Livro,
    UsuarioLivro,
)


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "nome",
        "cpf",
        "rg",
    )

    search_fields = (
        "user__username",
        "nome",
        "cpf",
        "rg",
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
        "usuario__user__username",
        "livro__titulo",
    )

    list_filter = ("data_hora",)