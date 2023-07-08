from django.urls import path

from . import views

app_name = "alunos"

urlpatterns = [
    path("perfil/", views.perfil, name="perfil"),
]
