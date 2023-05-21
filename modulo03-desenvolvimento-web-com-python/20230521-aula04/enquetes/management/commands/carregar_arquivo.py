import json
import os

from django.core.management.base import BaseCommand
from django.utils import timezone

from enquetes.models import Pergunta, Opcao


class Command(BaseCommand):
    help = "Carrega as enquetes de um arquivo e salva no banco de dados"

    def add_arguments(self, parser):
        parser.add_argument("arquivo", nargs=1, type=str)

    
    def handle(self, *args, **options):
        
        arquivo = options.get("arquivo")[0]
        caminho_arquivo = os.path.join(os.getcwd(), "dados", arquivo)

        with open(caminho_arquivo, "r", encoding="utf-8") as _f:

            conteudo_arquivo = json.load(_f)

            for pergunta, opcoes in conteudo_arquivo.items():
                
                pergunta_obj = Pergunta(
                    texto=pergunta,
                    data_de_publicacao=timezone.now()
                )

                pergunta_obj.save()

                for opcao in opcoes:
                    Opcao(texto=opcao["texto"], pergunta=pergunta_obj).save()
