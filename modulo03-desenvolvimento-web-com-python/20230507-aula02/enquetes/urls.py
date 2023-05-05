from django.urls import path

# O ponto (.) significa que iremos importar o módulo views que se encontra no mesmo
# diretório que o módulo urls
from . import views

urlpatterns = [
    path("numero-da-sorte/", views.numero_da_sorte, name="numero_da_sorte"),
    path("", views.index, name="index"),
]
