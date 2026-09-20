from django.urls import path

from . import views

app_name = "biblioteca"

urlpatterns = [
    path(
        "categorias/",
        views.categoria_listar,
        name="categoria_listar",
    ),
    path(
        "categorias/cadastrar/",
        views.categoria_criar,
        name="categoria_criar",
    ),
    path(
        "categorias/<int:id>/",
        views.categoria_detalhar,
        name="categoria_detalhar",
    ),
    path(
        "categorias/<int:id>/editar/",
        views.categoria_editar,
        name="categoria_editar",
    ),
    path(
        "categorias/<int:id>/excluir/",
        views.categoria_excluir,
        name="categoria_excluir",
    ),
]