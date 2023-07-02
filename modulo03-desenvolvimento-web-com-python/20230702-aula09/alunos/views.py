from django.shortcuts import render

def perfil(request):

    lista_de_turmas_que_esta_matriculado = request.user.aluno.all()
    
    return render(
        request,
        "perfil.html",
        {"lista_de_turmas_que_esta_matriculado": lista_de_turmas_que_esta_matriculado}
    )
