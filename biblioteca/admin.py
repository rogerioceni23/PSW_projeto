from django.contrib import admin

from .models import (
    Usuario,
    Autor,
    Categoria,
    Livro,
    Avaliacao,
    Perfil,
)


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "is_staff",
        "is_active",
    )

    search_fields = (
        "username",
        "email",
    )

    list_filter = (
        "is_staff",
        "is_active",
    )


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "data_nascimento",
    )

    search_fields = (
        "nome",
    )


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
    )

    search_fields = (
        "nome",
    )


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

    list_filter = (
        "ano_publicacao",
    )

    filter_horizontal = (
        "autores",
        "categorias",
    )


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "livro",
        "usuario",
        "nota",
        "data_criacao",
    )

    search_fields = (
        "livro__titulo",
        "usuario__username",
        "comentario",
    )

    list_filter = (
        "nota",
        "data_criacao",
    )


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "usuario",
    )

    search_fields = (
        "usuario__username",
    )