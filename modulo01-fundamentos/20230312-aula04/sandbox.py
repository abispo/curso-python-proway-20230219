"""
Para instalar o pacote faker, abra o terminal e digita pip install -r requirements.txt.
Faça isso de preferência dentro de um virtualenv

"""

import csv
import os

import faker
from faker.providers import python

fake = faker.Faker('pt_BR')
fake.add_provider(python)

files_directory = os.path.join(os.getcwd(), "files")

if __name__ == "__main__":

    with open(os.path.join(files_directory, "notas.csv"), "w", encoding="utf-8") as _file:
        fieldnames = ["nome", "n1", "n2", "n3", "n4", "n5"]
        csv_writer = csv.DictWriter(_file, fieldnames=fieldnames, delimiter=";")
        csv_writer.writeheader()
        for _ in range(100):
            data = {
                "nome": fake.first_name(),
                "n1": fake.pyint(min_value=0, max_value=10),
                "n2": fake.pyint(min_value=0, max_value=10),
                "n3": fake.pyint(min_value=0, max_value=10),
                "n4": fake.pyint(min_value=0, max_value=10),
                "n5": fake.pyint(min_value=0, max_value=10),
            }

            csv_writer.writerow(data)

    with open(os.path.join(files_directory, "vendas.txt"), "w", encoding="utf-8", newline='') as _file:
        for contador in range(100):
            codigo = str(contador+1).zfill(4)
            line = [
                f"Código: {codigo}\n",
                f"Vendedor: {fake.first_name()} {fake.last_name()}\n",
                f"Vendas: {fake.pyfloat(left_digits=5, right_digits=2, positive=True, min_value=3000, max_value=20000)}\n\n"
            ]
            _file.writelines(line)

    with open(os.path.join(files_directory, "nomes.txt"), "w", encoding="utf-8") as _file:
        for _ in range(10000):
            _file.write(f"{fake.first_name()}\n")