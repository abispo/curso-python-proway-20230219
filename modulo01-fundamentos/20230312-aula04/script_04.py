"""
Trabalhando com arquivos .csv no Python

writer e DictWriter

https://docs.python.org/3/library/csv.html

CSV -> Comma Separated Values -> Valores Separados por Vírgula
"""

import csv
import os

if __name__ == "__main__":
    

    with open(os.path.join(os.getcwd(), "clientes.csv"), "w", newline="") as arquivo:

        # Lista dos registros que serão salvos no arquivo clientes.csv
        lista_clientes = (
            ["Maria", 20, "F"],
            ["Carla", 21, "F"],
            ["João", 25, "M"],
        )

        # Criar o objeto writer
        writer = csv.writer(arquivo, delimiter=";")

        # Escrever no arquivo o cabeçalho
        writer.writerow(["nome", "idade", "sexo"])
        writer.writerow(["Daniele", 30, "F"])

        # Escrevemos os registros no arquivo utilizando o método writerows
        # Temos que passar uma lista de listas para o método
        writer.writerows(lista_clientes)

    with open(os.path.join(os.getcwd(), "clientes2.csv"), "w", newline="") as arquivo:

        # Lista dos registros que serão salvos
        lista_acessos = [
            {"nome": "Maria", "ultimo_acesso": "20221201"},
            {"nome": "Carla", "ultimo_acesso": "20221202"},
            {"nome": "Barbara", "ultimo_acesso": "20221205"},
            {"nome": "Amanda", "ultimo_acesso": "20221208"},
            {"nome": "Thais", "ultimo_acesso": "20221211"},
        ]

        # Nomes das colunas do arquivo csv
        fieldnames = ["nome", "ultimo_acesso"]

        dict_writer = csv.DictWriter(arquivo, fieldnames=fieldnames, delimiter=";")

        dict_writer.writeheader()

        dict_writer.writerow({"nome": "Julia", "ultimo_acesso": "20221215"})

        dict_writer.writerows(lista_acessos)
