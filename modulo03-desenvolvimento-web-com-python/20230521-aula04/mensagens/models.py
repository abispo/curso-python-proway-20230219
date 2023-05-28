from django.db import models

from enquetes.models import Pergunta


class Mensagem(models.Model):

    email = models.CharField(max_length=100, null=True, blank=True)
    texto = models.TextField(null=False)
    data_hora = models.DateTimeField(auto_now_add=True)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.texto

    class Meta:
        db_table = "tb_mensagens"
