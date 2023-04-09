import sqlite3

def excluir_tabelas(cursor):
    
    tabelas = ["tb_pedidos_itens", "tb_pedidos", "tb_produtos"]

    for tabela in tabelas:
        comando = f"DROP TABLE IF EXISTS {tabela};"
        cursor.execute(comando)

def criar_tabela_produtos(cursor):

    comando = """
    CREATE TABLE IF NOT EXISTS tb_produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL
    );
    """

    cursor.execute(comando)

    print("Tabela tb_produtos criada com sucesso!")
    

def criar_tabela_pedidos(cursor):

    comando = """
    CREATE TABLE IF NOT EXISTS tb_pedidos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_hora TIMESTAMP NOT NULL,
        observacoes TEXT
    );
    """

    cursor.execute(comando)
    print("Tabela tb_pedidos criada com sucesso!")


def criar_tabela_pedidos_itens(cursor):

    comando = """
    CREATE TABLE IF NOT EXISTS tb_pedidos_itens(
        pedido_id INTEGER NOT NULL,
        produto_id INTEGER NOT NULL,
        quantidade INTEGER NOT NULL,
        PRIMARY KEY(pedido_id, produto_id),
        FOREIGN KEY(pedido_id) REFERENCES tb_pedidos(id),
        FOREIGN KEY(produto_id) REFERENCES tb_produtos(id)
    );
    """

    cursor.execute(comando)
    print("Tabela tb_pedidos_itens criada com sucesso!")


def popular_tb_produtos(cursor):
    # Dicionário com os produtos
    produtos = [
        {"nome": "Pastel", "preco": 9.90},
        {"nome": "Coxinha", "preco": 5},
        {"nome": "Rolinho de Salsicha", "preco": 5},
        {"nome": "Cachorro-Quente", "preco": 10},
        {"nome": "Risoles", "preco": 8}
    ]

    for produto in produtos:
        nome = produto.get("nome")
        preco = produto.get("preco")

        comando = f"INSERT INTO tb_produtos(nome, preco) VALUES('{nome}', '{preco}')"

        resultado = cursor.execute(comando)
        print(f"O produto {nome} foi inserido com sucesso!")


if __name__ == "__main__":
    
    conexao = sqlite3.connect("db.sqlite3")
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")
 
    criar_tabela_produtos(cursor)
    criar_tabela_pedidos(cursor)
    criar_tabela_pedidos_itens(cursor)

    popular_tb_produtos(cursor)
    conexao.commit()

    saida = """
    Sistema de Pedidos. Escolha a sua opção:
    1 - Cadastrar novo Pedido
    2 - Visualizar os Pedidos
    3 - Sair
    """

    while True:
        
        print(saida)
        
        try:
            opcao = int(input("OPÇÃO: "))

            if opcao == 1:
                # Para cadastrar um novo pedido, é interessante mostrar a lista de produtos disponíveis
                # Também colocar uma validação que verifica se o ID do produto existe

                # Quando um pedido for finalizado, devemos salvar os dados em 2 tabelas:
                # tb_pedidos, tb_pedidos_itens

                # Quando o registro for inserido na tb_pedidos, vamos pegar o ID desse registro, que
                # é feito pegando o atributo lastrowid do objeto cursor 'r' gerado (r = cursor.execute(comand))

                # Após isso, vamos salvar na tabela tb_pedidos_itens esse id do pedido, e os ids dos produtos
                # escolhidos pelo usuário

                pass

            elif opcao == 2:
                # Será mostrada a lista de pedidos, contendo:
                # ID do Pedido
                # Os produtos que fazem parte desse pedido
                # O total do pedido

                pass

            elif opcao == 3:
                break

            else:
                print(f"A opção {opcao} não foi encontrada. Informe novamente.")

        except ValueError:
            print("Você deve informar uma opção válida")

    # Comente a linha abaixo quando não quiser que as tabelas sejam excluídas ao final da execução
    # do script
    excluir_tabelas(cursor)
