from django.core.management.base import BaseCommand

class Command(BaseCommand):
    # Texto que aparece na ajuda do comando
    help = "Informações sobre o projeto"

    # O método handle é responsável por executar o código do comando chamado
    def handle(self, *args, **options):
        saida = """
        Sistema de enquetes
        Proway 2023
        """

        self.stdout.write(saida)
