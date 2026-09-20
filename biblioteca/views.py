from django.shortcuts import get_object_or_404, redirect, render

from .forms import AutorForm, CategoriaForm
from .models import Autor, Categoria

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