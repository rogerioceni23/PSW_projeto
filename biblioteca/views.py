from django.shortcuts import redirect, render

from .forms import AutorForm, CategoriaForm
from .models import Livro


def inicio(request):
    return render(request, "biblioteca/inicio.html")


def listar_livros(request):
    livros = Livro.objects.all().order_by("titulo")

    return render(
        request,
        "biblioteca/listar_livros.html",
        {"livros": livros},
    )


def criar_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("biblioteca:criar_categoria")
    else:
        form = CategoriaForm()

    return render(
        request,
        "biblioteca/criar_categoria.html",
        {"form": form},
    )


def criar_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("biblioteca:criar_autor")
    else:
        form = AutorForm()

    return render(
        request,
        "biblioteca/criar_autor.html",
        {"form": form},
    )