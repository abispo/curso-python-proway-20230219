from django.db import models


class Pergunta(models.Model):

    texto = models.CharField(max_length=200)
    data_de_publicacao = models.DateTimeField("Data de publicação")


    # A classe Meta representa as configurações da model
    class Meta:
        db_table = "tb_perguntas"

    def __str__(self):
        return self.texto


class Opcao(models.Model):

    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    class Meta:
        db_table = "tb_opcoes"

    def __str__(self) -> str:
        return self.texto
