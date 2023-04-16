
from database import session, Base, engine
from models import Usuario, UsuarioPerfil

def criar_usuario(email, senha, nome, sexo):

    usuario = Usuario(
        email=email, senha=senha
    )

    session.add(usuario)
    session.commit()

    criar_perfil_usuario(usuario, nome, sexo)


def criar_perfil_usuario(usuario, nome, sexo):

    perfil_usuario = UsuarioPerfil(
        id=usuario.id,
        nome=nome,
        sexo=sexo
    )

    session.add(perfil_usuario)
    session.commit()


if __name__ == "__main__":
    criar_usuario("ana@email.com", "123456", "Ana", "F")
