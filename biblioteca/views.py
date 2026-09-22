from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import Group

from .forms import (
    AutorForm,
    CategoriaForm,
    LivroForm,
    UsuarioCriacaoForm,
    UsuarioEdicaoForm,
    UsuarioLivroForm,
    CadastroLeitorForm,
)
from .models import Autor, Categoria, Livro, Usuario, UsuarioLivro

@login_required
@permission_required(
    "biblioteca.view_usuario",
    raise_exception=True,
)
def painel(request):
    contexto = {
        "quantidade_livros": Livro.objects.count(),
        "quantidade_autores": Autor.objects.count(),
        "quantidade_categorias": Categoria.objects.count(),
        "quantidade_usuarios": Usuario.objects.count(),
        "quantidade_vinculos": UsuarioLivro.objects.count(),
    }

    return render(
        request,
        "biblioteca/painel.html",
        contexto,
    )

def pagina_inicial(request):
    if request.user.is_authenticated:
        if request.user.has_perm("biblioteca.view_usuario"):
            return redirect("biblioteca:painel")

        return redirect("biblioteca:inicio")

    return render(
        request,
        "biblioteca/pagina_inicial.html",
    )

@login_required
def inicio(request):
    livros_recentes = Livro.objects.prefetch_related(
        "autores",
        "categorias",
    ).order_by("-id")[:6]

    quantidade_meus_livros = UsuarioLivro.objects.filter(
        usuario=request.user,
    ).count()

    contexto = {
        "livros_recentes": livros_recentes,
        "quantidade_meus_livros": quantidade_meus_livros,
    }

    return render(
        request,
        "biblioteca/leitor/inicio.html",
        contexto,
    )

def cadastrar_leitor(request):
    if request.user.is_authenticated:
        return redirect("biblioteca:livro_listar")

    if request.method == "POST":
        form = CadastroLeitorForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            usuario = form.save()

            grupo_leitor, _ = Group.objects.get_or_create(
                name="Leitor",
            )

            usuario.groups.add(grupo_leitor)

            messages.success(
                request,
                "Conta criada com sucesso. Agora você pode entrar.",
            )

            return redirect("biblioteca:entrar")
    else:
        form = CadastroLeitorForm()

    return render(
        request,
        "biblioteca/autenticacao/cadastrar.html",
        {"form": form},
    )

def entrar(request):
    if request.user.is_authenticated:
        if request.user.has_perm("biblioteca.view_usuario"):
            return redirect("biblioteca:painel")

        return redirect("biblioteca:inicio")

    form = AuthenticationForm(
        request,
        data=request.POST or None,
    )

    form.fields["username"].widget.attrs.update(
        {
            "class": "form-control",
            "placeholder": "Digite seu usuário",
            "autocomplete": "username",
        }
    )

    form.fields["password"].widget.attrs.update(
        {
            "class": "form-control",
            "placeholder": "Digite sua senha",
            "autocomplete": "current-password",
        }
    )

    if request.method == "POST" and form.is_valid():
        usuario = form.get_user()
        login(request, usuario)

        messages.success(
            request,
            "Login realizado com sucesso.",
        )

        if usuario.has_perm("biblioteca.view_usuario"):
            return redirect("biblioteca:painel")

        return redirect("biblioteca:inicio")

    return render(
        request,
        "biblioteca/autenticacao/entrar.html",
        {"form": form},
    )

@login_required
def sair(request):
    if request.method == "POST":
        logout(request)

        messages.success(
            request,
            "Você saiu do sistema.",
        )

        return redirect("biblioteca:entrar")

    return redirect("biblioteca:livro_listar")


# CRUD de categorias


@login_required
@permission_required("biblioteca.view_categoria", raise_exception=True)
def categoria_listar(request):
    categorias = Categoria.objects.all()

    return render(
        request,
        "biblioteca/categoria/listar.html",
        {"categorias": categorias},
    )


@login_required
@permission_required("biblioteca.add_categoria", raise_exception=True)
def categoria_criar(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Categoria cadastrada com sucesso.",
            )

            return redirect("biblioteca:categoria_listar")
    else:
        form = CategoriaForm()

    return render(
        request,
        "biblioteca/categoria/formulario.html",
        {"form": form},
    )


@login_required
@permission_required("biblioteca.view_categoria", raise_exception=True)
def categoria_detalhar(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    return render(
        request,
        "biblioteca/categoria/detalhar.html",
        {"categoria": categoria},
    )


@login_required
@permission_required("biblioteca.change_categoria", raise_exception=True)
def categoria_editar(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == "POST":
        form = CategoriaForm(
            request.POST,
            instance=categoria,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Categoria atualizada com sucesso.",
            )

            return redirect("biblioteca:categoria_listar")
    else:
        form = CategoriaForm(instance=categoria)

    return render(
        request,
        "biblioteca/categoria/formulario.html",
        {
            "form": form,
            "categoria": categoria,
        },
    )


@login_required
@permission_required("biblioteca.delete_categoria", raise_exception=True)
def categoria_excluir(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == "POST":
        categoria.delete()

        messages.success(
            request,
            "Categoria excluída com sucesso.",
        )

        return redirect("biblioteca:categoria_listar")

    return render(
        request,
        "biblioteca/categoria/confirmar_exclusao.html",
        {"categoria": categoria},
    )


# CRUD de autores


@login_required
@permission_required("biblioteca.view_autor", raise_exception=True)
def autor_listar(request):
    autores = Autor.objects.all()

    return render(
        request,
        "biblioteca/autor/listar.html",
        {"autores": autores},
    )


@login_required
@permission_required("biblioteca.add_autor", raise_exception=True)
def autor_criar(request):
    if request.method == "POST":
        form = AutorForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Autor cadastrado com sucesso.",
            )

            return redirect("biblioteca:autor_listar")
    else:
        form = AutorForm()

    return render(
        request,
        "biblioteca/autor/formulario.html",
        {"form": form},
    )


@login_required
@permission_required("biblioteca.view_autor", raise_exception=True)
def autor_detalhar(request, id):
    autor = get_object_or_404(Autor, id=id)

    return render(
        request,
        "biblioteca/autor/detalhar.html",
        {"autor": autor},
    )


@login_required
@permission_required("biblioteca.change_autor", raise_exception=True)
def autor_editar(request, id):
    autor = get_object_or_404(Autor, id=id)

    if request.method == "POST":
        form = AutorForm(
            request.POST,
            instance=autor,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Autor atualizado com sucesso.",
            )

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


@login_required
@permission_required("biblioteca.delete_autor", raise_exception=True)
def autor_excluir(request, id):
    autor = get_object_or_404(Autor, id=id)

    if request.method == "POST":
        autor.delete()

        messages.success(
            request,
            "Autor excluído com sucesso.",
        )

        return redirect("biblioteca:autor_listar")

    return render(
        request,
        "biblioteca/autor/confirmar_exclusao.html",
        {"autor": autor},
    )


# CRUD de livros


@login_required
@permission_required("biblioteca.view_livro", raise_exception=True)
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


@login_required
@permission_required("biblioteca.add_livro", raise_exception=True)
def livro_criar(request):
    if request.method == "POST":
        form = LivroForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Livro cadastrado com sucesso.",
            )

            return redirect("biblioteca:livro_listar")
    else:
        form = LivroForm()

    return render(
        request,
        "biblioteca/livro/formulario.html",
        {"form": form},
    )


@login_required
@permission_required("biblioteca.view_livro", raise_exception=True)
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


@login_required
@permission_required("biblioteca.change_livro", raise_exception=True)
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

            messages.success(
                request,
                "Livro atualizado com sucesso.",
            )

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


@login_required
@permission_required("biblioteca.delete_livro", raise_exception=True)
def livro_excluir(request, id):
    livro = get_object_or_404(Livro, id=id)

    if request.method == "POST":
        livro.delete()

        messages.success(
            request,
            "Livro excluído com sucesso.",
        )

        return redirect("biblioteca:livro_listar")

    return render(
        request,
        "biblioteca/livro/confirmar_exclusao.html",
        {"livro": livro},
    )


# CRUD de usuários


@login_required
@permission_required("biblioteca.view_usuario", raise_exception=True)
def usuario_listar(request):
    usuarios = Usuario.objects.prefetch_related("groups").all()

    return render(
        request,
        "biblioteca/usuario/listar.html",
        {"usuarios": usuarios},
    )


@login_required
@permission_required("biblioteca.add_usuario", raise_exception=True)
def usuario_criar(request):
    if request.method == "POST":
        form = UsuarioCriacaoForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Usuário cadastrado com sucesso.",
            )

            return redirect("biblioteca:usuario_listar")
    else:
        form = UsuarioCriacaoForm()

    return render(
        request,
        "biblioteca/usuario/formulario.html",
        {"form": form},
    )


@login_required
@permission_required("biblioteca.view_usuario", raise_exception=True)
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


@login_required
@permission_required("biblioteca.change_usuario", raise_exception=True)
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

            messages.success(
                request,
                "Usuário atualizado com sucesso.",
            )

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


@login_required
@permission_required("biblioteca.delete_usuario", raise_exception=True)
def usuario_excluir(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    if request.method == "POST":
        usuario.delete()

        messages.success(
            request,
            "Usuário excluído com sucesso.",
        )

        return redirect("biblioteca:usuario_listar")

    return render(
        request,
        "biblioteca/usuario/confirmar_exclusao.html",
        {"usuario": usuario},
    )


# CRUD dos vínculos entre usuários e livros


@login_required
@permission_required("biblioteca.view_usuariolivro", raise_exception=True)
def usuario_livro_listar(request):
    vinculos = UsuarioLivro.objects.select_related(
        "usuario",
        "livro",
    ).all()

    return render(
        request,
        "biblioteca/usuario_livro/listar.html",
        {"vinculos": vinculos},
    )


@login_required
@permission_required("biblioteca.add_usuariolivro", raise_exception=True)
def usuario_livro_criar(request):
    if request.method == "POST":
        form = UsuarioLivroForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Vínculo cadastrado com sucesso.",
            )

            return redirect("biblioteca:usuario_livro_listar")
    else:
        form = UsuarioLivroForm()

    return render(
        request,
        "biblioteca/usuario_livro/formulario.html",
        {"form": form},
    )


@login_required
@permission_required("biblioteca.view_usuariolivro", raise_exception=True)
def usuario_livro_detalhar(request, id):
    vinculo = get_object_or_404(
        UsuarioLivro.objects.select_related(
            "usuario",
            "livro",
        ),
        id=id,
    )

    return render(
        request,
        "biblioteca/usuario_livro/detalhar.html",
        {"vinculo": vinculo},
    )


@login_required
@permission_required(
    "biblioteca.change_usuariolivro",
    raise_exception=True,
)
def usuario_livro_editar(request, id):
    vinculo = get_object_or_404(UsuarioLivro, id=id)

    if request.method == "POST":
        form = UsuarioLivroForm(
            request.POST,
            instance=vinculo,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Vínculo atualizado com sucesso.",
            )

            return redirect("biblioteca:usuario_livro_listar")
    else:
        form = UsuarioLivroForm(instance=vinculo)

    return render(
        request,
        "biblioteca/usuario_livro/formulario.html",
        {
            "form": form,
            "vinculo": vinculo,
        },
    )


@login_required
@permission_required(
    "biblioteca.delete_usuariolivro",
    raise_exception=True,
)
def usuario_livro_excluir(request, id):
    vinculo = get_object_or_404(UsuarioLivro, id=id)

    if request.method == "POST":
        vinculo.delete()

        messages.success(
            request,
            "Vínculo excluído com sucesso.",
        )

        return redirect("biblioteca:usuario_livro_listar")

    return render(
        request,
        "biblioteca/usuario_livro/confirmar_exclusao.html",
        {"vinculo": vinculo},
    )

def erro_permissao(request, exception=None):
    return render(
        request,
        "biblioteca/erros/403.html",
        status=403,
    )

@login_required
def meus_livros(request):
    vinculos = UsuarioLivro.objects.filter(
        usuario=request.user,
    ).select_related(
        "livro",
    ).prefetch_related(
        "livro__autores",
        "livro__categorias",
    ).order_by("-data_hora")

    return render(
        request,
        "biblioteca/leitor/meus_livros.html",
        {"vinculos": vinculos},
    )