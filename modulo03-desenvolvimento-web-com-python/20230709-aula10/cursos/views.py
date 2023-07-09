from django.shortcuts import render

# import absoluto
from cursos.models import Curso

# import relativo
# from .models import Curso

def mostrar_todos_cursos(request):
    
    todos_os_cursos = Curso.objects.all()

    contexto = {"todos_os_cursos": todos_os_cursos}

    return render(request, "todos_os_cursos.html", contexto)
