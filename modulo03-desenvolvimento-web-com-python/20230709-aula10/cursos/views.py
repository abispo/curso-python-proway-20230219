from django.shortcuts import render, get_object_or_404

# import absoluto
from cursos.models import Curso

# import relativo
# from .models import Curso

def mostrar_todos_cursos(request):
    
    todos_os_cursos = Curso.objects.all()

    contexto = {"todos_os_cursos": todos_os_cursos}

    return render(request, "todos_os_cursos.html", contexto)


def detalhe_do_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)

    lista_de_turmas = curso.turma_set.filter(aceitando_matriculas=True)

    contexto = {"lista_de_turmas": lista_de_turmas}

    return render(request, "detalhe_curso.html", contexto)
