from django.urls import path

# O ponto (.) significa que iremos importar o módulo views que se encontra no mesmo
# diretório que o módulo urls
from . import views

# namespace
app_name = "enquetes"

urlpatterns = [
    path("numero-da-sorte/", views.numero_da_sorte, name="numero_da_sorte"),
    path("", views.index, name="index"),
    path("<int:pergunta_id>/", views.detalhes, name="detalhes"),
    path("<int:pergunta_id>/resultados/", views.resultados, name="resultados"),
    path("<int:pergunta_id>/votar/", views.votar, name="votar"),
    path("estatisticas/", views.estatisticas, name="estatisticas"),
    path("<int:pergunta_id>/nova_mensagem/", views.nova_mensagem, name="nova_mensagem"),
]
