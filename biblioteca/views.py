from django.shortcuts import get_object_or_404, redirect, render
from .models import Autor, Categoria, Livro
from .forms import (
    AutorForm,
    CategoriaForm,
    LivroForm,
    UsuarioCriacaoForm,
    UsuarioEdicaoForm,
)
from .models import Autor, Categoria, Livro, Usuario

def categoria_listar(request):
    categorias = Categoria.objects.all()

    contexto = {
        "categorias": categorias,
    }

    return render(
        request,
        "biblioteca/categoria/listar.html",
        contexto,
    )

def categoria_criar(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("biblioteca:categoria_listar")
    else:
        form = CategoriaForm()

    contexto = {
        "form": form,
    }

    return render(
        request,
        "biblioteca/categoria/formulario.html",
        contexto,
    )

def categoria_detalhar(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    contexto = {
        "categoria": categoria,
    }

    return render(
        request,
        "biblioteca/categoria/detalhar.html",
        contexto,
    )


def categoria_editar(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == "POST":
        form = CategoriaForm(
            request.POST,
            instance=categoria,
        )

        if form.is_valid():
            form.save()
            return redirect("biblioteca:categoria_listar")
    else:
        form = CategoriaForm(instance=categoria)

    contexto = {
        "form": form,
        "categoria": categoria,
    }

    return render(
        request,
        "biblioteca/categoria/formulario.html",
        contexto,
    )


def categoria_excluir(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == "POST":
        categoria.delete()
        return redirect("biblioteca:categoria_listar")

    contexto = {
        "categoria": categoria,
    }

    return render(
        request,
        "biblioteca/categoria/confirmar_exclusao.html",
        contexto,
    )
def autor_listar(request):
    autores = Autor.objects.all()

    return render(
        request,
        "biblioteca/autor/listar.html",
        {"autores": autores},
    )


def autor_criar(request):
    if request.method == "POST":
        form = AutorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("biblioteca:autor_listar")
    else:
        form = AutorForm()

    return render(
        request,
        "biblioteca/autor/formulario.html",
        {"form": form},
    )


def autor_detalhar(request, id):
    autor = get_object_or_404(Autor, id=id)

    return render(
        request,
        "biblioteca/autor/detalhar.html",
        {"autor": autor},
    )


def autor_editar(request, id):
    autor = get_object_or_404(Autor, id=id)

    if request.method == "POST":
        form = AutorForm(request.POST, instance=autor)

        if form.is_valid():
            form.save()
            return redirect("biblioteca:autor_listar")
    else:
        form = AutorForm(instance=autor)

    return render(
        request,
        "biblioteca/autor/formulario.html",
        {
            "form": form,
            "autor": autor,
        },
    )


def autor_excluir(request, id):
    autor = get_object_or_404(Autor, id=id)

    if request.method == "POST":
        autor.delete()
        return redirect("biblioteca:autor_listar")

    return render(
        request,
        "biblioteca/autor/confirmar_exclusao.html",
        {"autor": autor},
    )

def livro_listar(request):
    livros = Livro.objects.prefetch_related(
        "autores",
        "categorias",
    ).all()

    return render(
        request,
        "biblioteca/livro/listar.html",
        {"livros": livros},
    )


def livro_criar(request):
    if request.method == "POST":
        form = LivroForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            form.save()
            return redirect("biblioteca:livro_listar")
    else:
        form = LivroForm()

    return render(
        request,
        "biblioteca/livro/formulario.html",
        {"form": form},
    )


def livro_detalhar(request, id):
    livro = get_object_or_404(
        Livro.objects.prefetch_related(
            "autores",
            "categorias",
        ),
        id=id,
    )

    return render(
        request,
        "biblioteca/livro/detalhar.html",
        {"livro": livro},
    )


def livro_editar(request, id):
    livro = get_object_or_404(Livro, id=id)

    if request.method == "POST":
        form = LivroForm(
            request.POST,
            request.FILES,
            instance=livro,
        )

        if form.is_valid():
            form.save()
            return redirect("biblioteca:livro_listar")
    else:
        form = LivroForm(instance=livro)

    return render(
        request,
        "biblioteca/livro/formulario.html",
        {
            "form": form,
            "livro": livro,
        },
    )


def livro_excluir(request, id):
    livro = get_object_or_404(Livro, id=id)

    if request.method == "POST":
        livro.delete()
        return redirect("biblioteca:livro_listar")

    return render(
        request,
        "biblioteca/livro/confirmar_exclusao.html",
        {"livro": livro},
    )

def usuario_listar(request):
    usuarios = Usuario.objects.prefetch_related("groups").all()

    return render(
        request,
        "biblioteca/usuario/listar.html",
        {"usuarios": usuarios},
    )


def usuario_criar(request):
    if request.method == "POST":
        form = UsuarioCriacaoForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            form.save()
            return redirect("biblioteca:usuario_listar")
    else:
        form = UsuarioCriacaoForm()

    return render(
        request,
        "biblioteca/usuario/formulario.html",
        {"form": form},
    )


def usuario_detalhar(request, id):
    usuario = get_object_or_404(
        Usuario.objects.prefetch_related("groups"),
        id=id,
    )

    return render(
        request,
        "biblioteca/usuario/detalhar.html",
        {"usuario": usuario},
    )


def usuario_editar(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    if request.method == "POST":
        form = UsuarioEdicaoForm(
            request.POST,
            request.FILES,
            instance=usuario,
        )

        if form.is_valid():
            form.save()
            return redirect("biblioteca:usuario_listar")
    else:
        form = UsuarioEdicaoForm(instance=usuario)

    return render(
        request,
        "biblioteca/usuario/formulario.html",
        {
            "form": form,
            "usuario": usuario,
        },
    )


def usuario_excluir(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    if request.method == "POST":
        usuario.delete()
        return redirect("biblioteca:usuario_listar")

    return render(
        request,
        "biblioteca/usuario/confirmar_exclusao.html",
        {"usuario": usuario},
    )
