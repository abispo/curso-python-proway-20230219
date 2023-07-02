from django.contrib.auth.models import User
from django.db import models

from cursos.models import Curso


class Turma(models.Model):

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    instrutor = models.ForeignKey(User, related_name="instrutor", on_delete=models.CASCADE)
    data_inicio = models.DateTimeField(null=False, blank=False)
    data_fim = models.DateTimeField(null=False, blank=False)
    qtd_minima_alunos = models.IntegerField(default=0)
    qtd_maxima_alunos = models.IntegerField(default=1000)
    alunos = models.ManyToManyField(User, related_name="aluno", db_table="tb_turmas_alunos")
    

    def __str__(self):
        return f"Turma {self.data_inicio.year}{self.id} {self.curso}"

    
    class Meta:
        db_table = "tb_turmas"
