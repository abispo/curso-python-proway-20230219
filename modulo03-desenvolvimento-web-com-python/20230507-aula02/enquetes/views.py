from random import randint

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

# enquetes/numero-da-sorte
def numero_da_sorte(request):
    numero_da_sorte = randint(1, 60)

    return HttpResponse(numero_da_sorte)


def index(request):
    
    return HttpResponse("Olá! Bem vindo ao sistema de enquetes.")
