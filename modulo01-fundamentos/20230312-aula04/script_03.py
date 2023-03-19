"""
Trabalhando com arquivos .csv no Python

reader e DictReader

CSV -> Comma Separated Values -> Valores Separados por Vírgula
"""

import csv
import os

if __name__ == "__main__":
    
    with open(os.path.join(os.getcwd(), "notas.csv"), "r") as arquivo:

        # Por padrão, o método reader considera que o separador padrão é a vírgula
        # Nesse caso, precisamos indicar que o separador padrão é o ponto-e-vírgula
        arquivo_csv = csv.reader(arquivo, delimiter=';')

        for linha in arquivo_csv:
            print(linha)

    with open(os.path.join(os.getcwd(), "notas.csv"), "r") as arquivo:

        arquivo_csv = csv.DictWriter(arquivo, delimiter=';')

        for linha in arquivo_csv:
            print(linha)
