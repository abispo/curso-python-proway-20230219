from django.urls import path

from . import views

app_name = "cursos"

urlpatterns = [
    path("", views.mostrar_todos_cursos, name="todos_os_cursos"),
]
