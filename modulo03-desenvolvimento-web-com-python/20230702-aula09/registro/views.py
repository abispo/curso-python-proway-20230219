from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils import timezone

from registro.forms import PreRegistroForm
from registro.models import PreRegistro
from registro.utils import enviar_email

from registro.validators import (
    dados_preenchidos, username_ou_email_ja_cadastrado, senha_valida
)

def registrar(request):

    if request.method == "GET":

        pre_registro = PreRegistro.objects.filter(uuid=request.GET.get("id")).first()

        error_message = None

        if not pre_registro:
            error_message = "Token de confirmação não encontrado!"

        elif not pre_registro.valido:
            error_message = "Token inválido."
    
        elif settings.PRE_REGISTRO_TIME_LIMIT < (timezone.now() - pre_registro.data_hora).total_seconds():
            error_message = "O Token expirou."
        
        if error_message:
            return render(
                request, "falha_confirmacao_pre_cadastro.html", {"error_message": error_message, "pre_registro": pre_registro}
            )

        return render(request, "registro.html", {"pre_registro": pre_registro})

    elif request.method == "POST":
        
        try:

            username = request.POST['username']
            email = request.POST['email']
            senha = request.POST['password1']
            confirmacao_senha = request.POST['password2']
            uuid_pre_registro = request.POST['uuid_pre_registro']

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

            pre_registro = PreRegistro.objects.get(uuid=uuid_pre_registro)
            pre_registro.valido = False
            pre_registro.save()

            return redirect("login")

        except Exception:
            pass


def pre_registro(request):

    if request.method == "GET":
        form = PreRegistroForm()

        return render(request, "pre_registro.html", {"form": form})
    
    elif request.method == "POST":
        
        form = PreRegistroForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data.get("email")
            
            email_ja_cadastrado = User.objects.filter(email=email)
            email_no_pre_cadastro = PreRegistro.objects.filter(email=email, valido=False)

            if email_ja_cadastrado or email_no_pre_cadastro:

                form.errors.update({
                    "Erro de Pré-cadastro": "O e-mail informado é inválido. Verifique se o e-mail já não está cadastrado ou faz parte do pré-cadastro."
                })

                return render(request, "pre_registro.html", {"form": form})


            pre_registro = PreRegistro(email=email)
            pre_registro.save()

            enviar_email(pre_registro)

            return render(request, "envio_pre_cadastro.html")


def reenviar_pre_registro(request, uuid):
    if request.method == "GET":
        pre_registro = PreRegistro.objects.get(uuid=uuid)
        pre_registro.valido = False
        pre_registro.save()

        pre_registro = PreRegistro(email=pre_registro.email)
        pre_registro.save()

        enviar_email(pre_registro)

        return render(request, "envio_pre_cadastro.html")


def processar_login(request):
    usuario = request.user

    if usuario.groups.filter(name="alunos").exists():
        return redirect("alunos:profile")

    else:
        return redirect("login")
