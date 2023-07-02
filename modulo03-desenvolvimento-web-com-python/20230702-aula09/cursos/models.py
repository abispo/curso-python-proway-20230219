"""
Curso (model)
        - nome              texto (CharField)
        - carga_horaria     float
        - preco             float
        - descricao         text  (TextField)

        Os campos não podem ser nulos nem em branco
        o nome da tabela no banco deve ser tb_cursos

        python manage.py makemigrations
        python manage.py migrate

"""

from django.db import models


class Curso(models.Model):

    nome = models.CharField(max_length=200, null=False, blank=False)
    carga_horaria = models.FloatField(null=False, blank=False)
    preco = models.FloatField(null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "tb_cursos"