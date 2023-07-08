from django.core.mail import send_mail

def enviar_email(pre_registro):
    mensagem_email = f"""
        Você recebeu esse e-mail pois você ou alguém o cadastrou na escola de cursos. Caso queira confirmar o cadastro, clique no link a seguir.
        Caso não tenha sido você, apenas ignore esse e-mail.

        http://127.0.0.1:8000/registro/confirmacao?id={pre_registro.uuid}
    
    """

    send_mail(
        "Bem-vindo à escola de cursos",
        mensagem_email,
        "admin@localhost",
        [pre_registro.email]
    )
