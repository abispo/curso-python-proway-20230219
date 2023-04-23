
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


def listar_usuarios():

    # Consultar todos os registros (SELECT * FROM)
    resultado = session.query(Usuario).all()

    if len(resultado) == 0:
        print("Não há usuários cadastrados no sistema")


if __name__ == "__main__":

    while True:

        print("\nInforme a opção desejada: ")
        print("1 - Listar todos os usuários")
        print("2 - Cadastrar Usuário")
        print("3 - Excluir um usuário")
        print("4 - Atualizar os dados de um usuário")
        print("5 - SAIR")

        opcao = int(input("OPÇÃO: "))

        if opcao == 1:
            listar_usuarios()

        elif opcao == 2:
            
            email = input("Informe o e-mail do usuário: ")
            senha = input("Informe a senha do usuário: ")
            nome = input("Informe o nome do usuário: ")
            sexo = input("Informe o sexo do usuário: ")

            criar_usuario(email, senha, nome, sexo)
