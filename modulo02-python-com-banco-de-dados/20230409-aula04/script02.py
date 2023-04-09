import sqlite3

# Dicionário com os produtos
produtos = [
    {"nome": "Pastel", "preco": 9.90},
    {"nome": "Coxinha", "preco": 5},
    {"nome": "Rolinho de Salsicha", "preco": 5},
    {"nome": "Cachorro-Quente", "preco": 10},
    {"nome": "Risoles", "preco": 8}
]

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


if __name__ == "__main__":
    
    conexao = sqlite3.connect("db.sqlite3")
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")
 
    criar_tabela_produtos(cursor)
    criar_tabela_pedidos(cursor)
    criar_tabela_pedidos_itens(cursor)


    # Comente a linha abaixo quando não quiser que as tabelas sejam excluídas ao final da execução
    # do script
    excluir_tabelas(cursor)