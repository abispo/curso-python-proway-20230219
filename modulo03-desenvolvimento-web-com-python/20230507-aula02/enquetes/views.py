from random import randint

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from enquetes.models import Pergunta

# enquetes/numero-da-sorte
def numero_da_sorte(request):
    numero_da_sorte = randint(1, 60)

    return HttpResponse(numero_da_sorte)


def index(request):
    ultimas_cinco_perguntas = Pergunta.objects.order_by("-data_de_publicacao")[:5]
    
    template = loader.get_template("enquetes/index.html")
    contexto = {"ultimas_cinco_perguntas": ultimas_cinco_perguntas}

    return HttpResponse(template.render(contexto, request))

def detalhes(request, pergunta_id):
    return HttpResponse(f"Você está acessando os detalhes da pergunta {pergunta_id}")


def resultados(request, pergunta_id):
    return HttpResponse(f"Você está olhando os resultados pra pergunta {pergunta_id}")


def votar(request, pergunta_id):
    return HttpResponse(f"Você está votando na pergunta {pergunta_id}")