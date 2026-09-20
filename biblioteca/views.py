from django.shortcuts import get_object_or_404, redirect, render

from .forms import AutorForm, CategoriaForm, LivroForm
from .models import Autor, Categoria, Livro

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
