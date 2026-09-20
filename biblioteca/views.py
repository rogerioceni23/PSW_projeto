from django.shortcuts import get_object_or_404, redirect, render

from .models import Categoria
from .forms import CategoriaForm

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