import sqlite3

if __name__ == "__main__":

    conexao = sqlite3.connect("db.sqlite3")
    cursor = conexao.cursor()

    print("Criando a tabela tb_usuarios")
    comando = """
        CREATE TABLE IF NOT EXISTS tb_usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            senha TEXT NOT NULL
        );
    """
    cursor.execute(comando)

    print("Criando a tabela tb_usuarios_perfis")
    comando = """
    CREATE TABLE IF NOT EXISTS tb_usuarios_perfis(
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        sobrenome TEXT NOT NULL,
        idade INTEGER NULL,
        FOREIGN KEY(id) REFERENCES tb_usuarios(id)
    );
    """
    cursor.execute(comando)

    print("Criando a tabela tb_postagens")
    comando = """
    CREATE TABLE IF NOT EXISTS tb_postagens(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        titulo TEXT NOT NULL,
        corpo TEXT NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES tb_usuarios(id)
    );
    """
    cursor.execute(comando)

    print("Criando a tabela tb_categorias")
    comando = """
    CREATE TABLE IF NOT EXISTS tb_categorias(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    );
    """
    cursor.execute(comando)

    print("Criando a tabela tb_postagens_categorias")
    comando = """
    CREATE TABLE IF NOT EXISTS tb_postagens_categorias(
        postagem_id INTEGER NOT NULL,
        categoria_id INTEGER NOT NULL,
        PRIMARY KEY(postagem_id, categoria_id),
        FOREIGN KEY(postagem_id) REFERENCES tb_postagens(id),
        FOREIGN KEY(categoria_id) REFERENCES tb_categorias(id)
    );
    """
    cursor.execute(comando)
