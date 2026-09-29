# Biblioteca Digital

Projeto acadêmico em Django para consulta e gerenciamento de uma biblioteca digital. A aplicação usa views baseadas em função (FBVs), cinco CRUDs, autenticação do Django e uma interface adaptada do Tabler.

## Funcionalidades

- Página inicial pública, cadastro de leitor, entrada e saída da conta.
- Área do leitor para consultar livros, visualizar seus vínculos com livros e acessar o próprio perfil.
- Painel de gerenciamento próprio, com totais de livros, autores, categorias, usuários e vínculos.
- Cinco CRUDs: **Livro**, **Autor**, **Categoria**, **Usuario** e **UsuarioLivro**. Cada um possui listagem, cadastro, detalhes, edição e exclusão.
- Controle de acesso por grupos e pelas permissões `view`, `add`, `change` e `delete` dos modelos do Django.
- Upload de capas, PDFs e fotos para a pasta local `media/`.

`UsuarioLivro` registra a associação entre usuário e livro com data e hora. Essa associação não representa, por si só, um sistema de empréstimos ou devoluções.

## Tecnologias e interface

- Python, Django, Pillow e SQLite; as versões das dependências estão em `requirements.txt`.
- HTML com arquivos CSS e JavaScript do [Tabler](https://tabler.io/), mantidos em `biblioteca/static/tabler/`.
- Os arquivos HTML do Tabler foram adaptados para templates Django: carregamento de arquivos estáticos com `{% load static %}`, herança do layout, links com `{% url %}`, exibição de dados e formulários, proteção CSRF e visibilidade de menus conforme as permissões. O CSS e o JavaScript distribuídos pelo Tabler foram usados sem alterações.

## Estrutura dos dados

| Modelo | Papel no sistema |
| --- | --- |
| `Usuario` | Herda de `django.contrib.auth.models.User` e contém os dados adicionais do usuário. |
| `Livro` | Guarda título, descrição, ano, capa e PDF. |
| `Autor` | Guarda dados do autor; relaciona-se a livros em muitos para muitos. |
| `Categoria` | Classifica livros em uma relação muitos para muitos. |
| `UsuarioLivro` | Liga um usuário a um livro e registra a data e hora. |

`User`, `Group` e `Permission` fazem parte do sistema de autenticação do Django. `Usuario` estende `User`; o projeto não substitui `AUTH_USER_MODEL`.

## Instalação no Windows (PowerShell)

No diretório que contém `manage.py`, execute:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py createsuperuser
.\.venv\Scripts\python.exe manage.py runserver
```

Acesse `http://127.0.0.1:8000/`. O banco SQLite e os uploads são locais; cada integrante deve executar as migrações no próprio computador. Se já existir um banco local antigo com migrações incompatíveis, preserve os dados antes de recriá-lo.

## Grupos e permissões

O Django gera as permissões de cada modelo ao executar `migrate`. Configure os grupos no banco local antes de testar contas de leitor. Uma forma reproduzível, sem depender da interface administrativa padrão, é iniciar o shell:

```powershell
.\.venv\Scripts\python.exe manage.py shell
```

No shell Python, execute:

```python
from django.contrib.auth.models import Group, Permission

leitor, _ = Group.objects.get_or_create(name="Leitor")
leitor.permissions.set(
    Permission.objects.filter(
        content_type__app_label="biblioteca",
        codename__in=("view_livro", "view_autor", "view_categoria"),
    )
)

bibliotecario, _ = Group.objects.get_or_create(name="Bibliotecário")
bibliotecario.permissions.set(
    Permission.objects.filter(content_type__app_label="biblioteca")
)
```

Saia do shell com `exit()`. O grupo **Leitor** pode consultar livros, autores e categorias; o grupo **Bibliotecário** recebe as permissões dos cinco modelos da aplicação. O painel de gerenciamento exige a permissão de visualização de usuários. Uma conta criada pelo cadastro público deve receber o grupo Leitor; contas de gerenciamento devem receber o grupo Bibliotecário. A verificação de acesso ocorre nas views, e os menus também são exibidos conforme as permissões.

O superusuário criado pelo comando `createsuperuser` é uma conta administrativa inicial. Como `Usuario` herda do `User` padrão, esse comando cria um `User` básico; para uma conta com os campos adicionais de `Usuario`, use o cadastro correspondente na aplicação.

## Rotas principais

| Endereço | Uso |
| --- | --- |
| `/` | Página inicial pública. |
| `/entrar/` | Autenticação. |
| `/cadastrar/` | Cadastro público de leitor. |
| `/painel/` | Painel de gerenciamento. |
| `/livros/` | Listagem dos livros para quem tem permissão. |
| `/autores/` e `/categorias/` | Consulta e gerenciamento conforme permissões. |
| `/usuarios/` e `/usuarios-livros/` | Gerenciamento de usuários e de vínculos. |

As operações de criação, edição e exclusão dependem da permissão correspondente. A aplicação usa um painel próprio; o fluxo principal não depende da tela administrativa pronta do Django.

## Conferência rápida

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py showmigrations
```

Depois de iniciar o servidor, confira a página pública, o cadastro e login de leitor, o acesso do leitor ao catálogo e o bloqueio das operações administrativas. Com uma conta de gerenciamento, confira o painel e os cinco CRUDs, incluindo detalhes, formulários e exclusão.

## Colaboração

O código é compartilhado no mesmo repositório. Cada integrante sincroniza a branch `main` antes de trabalhar e registra somente suas próprias alterações em commits com mensagens claras. O histórico do Git mostra as contribuições efetivas de cada pessoa.

## Vídeo de demonstração

O vídeo apresenta as telas da aplicação, os cinco CRUDs
e os perfis de acesso de leitor e bibliotecário.

[Assistir à demonstração no YouTube](https://youtu.be/btfmiIFdayw)
