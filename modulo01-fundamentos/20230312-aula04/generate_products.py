"""
Para instalar o pacote faker, abra o terminal e digita pip install -r requirements.txt.
Faça isso de preferência dentro de um virtualenv

"""

import csv
import os

from random import choice
from uuid import uuid4

import faker
import faker_commerce
from faker.providers import python

fake = faker.Faker('pt_BR')
fake.add_provider(python)
fake.add_provider(faker_commerce.Provider)

files_directory = os.path.join(os.getcwd(), "files")

if __name__ == "__main__":

    with open(os.path.join(files_directory, "sales.csv"), "w", encoding="utf-8") as _file:
        sales_codes = [str(uuid4()) for _ in range(20)]
        fieldnames = ["sale_id", "product", "quantity", "price"]
        csv_writer = csv.DictWriter(_file, fieldnames=fieldnames, delimiter=";")
        csv_writer.writeheader()
        for _ in range(1000):
            data = {
                "sale_id": choice(sales_codes),
                "product": fake.ecommerce_name(),
                "quantity": fake.pyint(min_value=1, max_value=10),
                "price": fake.pyfloat(right_digits=2, positive=True, min_value=1, max_value=1000)
            }

            csv_writer.writerow(data)
