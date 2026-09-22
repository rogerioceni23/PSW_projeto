from django.urls import path

from . import views

app_name = "biblioteca"

urlpatterns = [

    path(
    	"",
    	views.pagina_inicial,
    	name="pagina_inicial",
    ),
    path(
    	"inicio/",
    	views.inicio,
    	name="inicio",
    ),

    path(
        "painel/",
        views.painel,
        name="painel",
    ),
    path(
        "entrar/",
        views.entrar,
        name="entrar",
    ),

    path(
    	"cadastrar/",
    	views.cadastrar_leitor,
    	name="cadastrar_leitor",
    ),

    path(
        "sair/",
        views.sair,
        name="sair",
    ),

    # Categorias
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

    # Autores
    path(
        "autores/",
        views.autor_listar,
        name="autor_listar",
    ),
    path(
        "autores/cadastrar/",
        views.autor_criar,
        name="autor_criar",
    ),
    path(
        "autores/<int:id>/",
        views.autor_detalhar,
        name="autor_detalhar",
    ),
    path(
        "autores/<int:id>/editar/",
        views.autor_editar,
        name="autor_editar",
    ),
    path(
        "autores/<int:id>/excluir/",
        views.autor_excluir,
        name="autor_excluir",
    ),

    # Livros
    path(
        "livros/",
        views.livro_listar,
        name="livro_listar",
    ),
    path(
        "livros/cadastrar/",
        views.livro_criar,
        name="livro_criar",
    ),
    path(
        "livros/<int:id>/",
        views.livro_detalhar,
        name="livro_detalhar",
    ),
    path(
        "livros/<int:id>/editar/",
        views.livro_editar,
        name="livro_editar",
    ),
    path(
        "livros/<int:id>/excluir/",
        views.livro_excluir,
        name="livro_excluir",
    ),

    # Usuários
    path(
        "usuarios/",
        views.usuario_listar,
        name="usuario_listar",
    ),
    path(
        "usuarios/cadastrar/",
        views.usuario_criar,
        name="usuario_criar",
    ),
    path(
        "usuarios/<int:id>/",
        views.usuario_detalhar,
        name="usuario_detalhar",
    ),
    path(
        "usuarios/<int:id>/editar/",
        views.usuario_editar,
        name="usuario_editar",
    ),
    path(
        "usuarios/<int:id>/excluir/",
        views.usuario_excluir,
        name="usuario_excluir",
    ),

    
    path(
        "usuarios-livros/",
        views.usuario_livro_listar,
        name="usuario_livro_listar",
    ),
    path(
        "usuarios-livros/cadastrar/",
        views.usuario_livro_criar,
        name="usuario_livro_criar",
    ),
    path(
        "usuarios-livros/<int:id>/",
        views.usuario_livro_detalhar,
        name="usuario_livro_detalhar",
    ),
    path(
        "usuarios-livros/<int:id>/editar/",
        views.usuario_livro_editar,
        name="usuario_livro_editar",
    ),
    path(
        "usuarios-livros/<int:id>/excluir/",
        views.usuario_livro_excluir,
        name="usuario_livro_excluir",
    ),

   path(
    	"meus-livros/",
    	views.meus_livros,
    	name="meus_livros",
   ),
]