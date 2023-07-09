from django.urls import path

from . import views

app_name = "cursos"

urlpatterns = [
    path("", views.mostrar_todos_cursos, name="todos_os_cursos"),
    path("<int:curso_id>/", views.detalhe_do_curso, name="detalhe_do_curso"),
]
