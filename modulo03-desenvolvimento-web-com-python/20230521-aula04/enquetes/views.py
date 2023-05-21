from random import randint

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from enquetes.models import Pergunta, Opcao

# enquetes/numero-da-sorte
def numero_da_sorte(request):
    numero_da_sorte = randint(1, 60)

    return HttpResponse(numero_da_sorte)


def index(request):
    ultimas_cinco_perguntas = Pergunta.objects.order_by("-data_de_publicacao")[:5]
    
    contexto = {
        "ultimas_cinco_perguntas": ultimas_cinco_perguntas
    }

    return render(request=request, template_name="enquetes/index.html", context=contexto)

def detalhes(request, pergunta_id):
    # pk = primary key
    # A função get_object_or_404 faz a consulta pelo registro com a pk informada.
    # Se não encontrar, gera um erro 404 NOT FOUND
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    return render(request, "enquetes/detalhes.html", {"pergunta": pergunta})


def resultados(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    return render(request, "enquetes/resultados.html", {"pergunta": pergunta})


def votar(request, pergunta_id):
    
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    try:
        opcao_selecionada = pergunta.opcao_set.get(pk=request.POST["opcao"])

    except (KeyError, Opcao.DoesNotExist):
        return render(
            request,
            "enquetes/detalhes.html",
            {
                "pergunta": pergunta,
                "mensagem_erro": "Você não escolheu uma opção válida!"
            }
        )

    else:
        opcao_selecionada.votos += 1
        opcao_selecionada.save()

        return HttpResponseRedirect(reverse("enquetes:resultados", args=(pergunta.id,)))
