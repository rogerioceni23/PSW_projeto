from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Cria e configura os grupos Bibliotecário e Leitor"

    def handle(self, *args, **options):
        permissoes_biblioteca = Permission.objects.filter(
            content_type__app_label="biblioteca",
        )

        grupo_bibliotecario, _ = Group.objects.get_or_create(
            name="Bibliotecário",
        )

        grupo_bibliotecario.permissions.set(
            permissoes_biblioteca,
        )

        grupo_leitor, _ = Group.objects.get_or_create(
            name="Leitor",
        )

        permissoes_leitor = Permission.objects.filter(
            content_type__app_label="biblioteca",
            codename__in=[
                "view_livro",
                "view_autor",
                "view_categoria",
            ],
        )

        grupo_leitor.permissions.set(
            permissoes_leitor,
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Grupos Bibliotecário e Leitor configurados com sucesso."
            )
        )