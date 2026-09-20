from django.urls import path

from . import views


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("livros/", views.listar_livros, name="listar_livros"),
    path(
        "categorias/cadastrar/",
        views.criar_categoria,
        name="criar_categoria",
    ),
    path(
        "autores/cadastrar/",
        views.criar_autor,
        name="criar_autor",
    ),
]