import os

from django.core.management.base import BaseCommand

import requests


class Command(BaseCommand):
    help = "Faz o download de um arquivo de enquetes"


    # O método add_arguments possibilita que definamos argumentos para o nosso comando
    def add_arguments(self, parser):

        # url   -> Nome do parâmetro
        # nargs -> Quantidade de valores que esse parâmetro recebe
        # type  -> Tipo dos valores do parâmetro
        parser.add_argument("url", nargs=1, type=str)


    def handle(self, *args, **options):
        url = options["url"][0]

        response = requests.get(url)

        data_dir = os.path.join(os.getcwd(), "dados")

        if not os.path.exists(data_dir):
            os.mkdir(data_dir)

        nome_arquivo = url.split("/")[-1]

        with open(os.path.join(data_dir, nome_arquivo), "w", encoding="utf-8") as _f:
            _f.write(response.text)

        self.stdout.write(f"Arquivo {nome_arquivo} salvo com sucesso.")