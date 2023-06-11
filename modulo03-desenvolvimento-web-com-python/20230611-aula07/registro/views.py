from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from registro.validators import (
    dados_preenchidos, username_ou_email_ja_cadastrado, senha_valida
)

def registrar(request):

    if request.method == "GET":
        return render(request, "registro.html")

    elif request.method == "POST":
        
        try:

            username = request.POST['username']
            email = request.POST['email']
            senha = request.POST['password1']
            confirmacao_senha = request.POST['password2']

            error_message = None

            if not dados_preenchidos(username, email, senha, confirmacao_senha):
                error_message = "Todos os campos são obrigatórios"

            elif username_ou_email_ja_cadastrado(username, email):
                error_message = "Existe algum problema no seu cadastro"

            elif not senha_valida(senha, confirmacao_senha):
                error_message = "As senhas não conferem."

            if error_message:
                return render(request, 'registro.html', {'error_message': error_message})
            
            User.objects.create_user(
                username=username, email=email, password=senha
            )

            return redirect("login")

        except Exception:
            pass