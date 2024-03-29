import sqlite3

if __name__ == "__main__":
    
    # O banco db.sqlite3 será criado no mesmo diretório onde está o arquivo
    conexao = sqlite3.connect("db.sqlite3")

    # Criamos o comando SQL e salvamos em uma variável
    comando = """
    CREATE TABLE IF NOT EXISTS tb_estados(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sigla TEXT NOT NULL
    );
    """

    # Criamos um cursor. O cursor é necessário para executar comandos no banco de dados, assim como
    # receber os resultados das consultas.
    cur = conexao.cursor()

    # Executa o comando
    cur.execute(comando)

    # https://dontpad.com/python-pedro

    estados = {
        "Acre": "AC", "Alagoas": "AL", "Amapá": "AP", "Amazonas": "AM",
        "Bahia": "BA", "Ceará": "CE", "Distrito Federal": "DF", "Espírito Santo": "ES",
        "Goiás": "GO", "Maranhão": "MA", "Mato Grosso": "MT",
        "Mato Grosso do Sul": "MS", "Minas Gerais": "MG", "Pará": "PA", "Paraíba": "PB",
        "Paraná": "PR", "Pernambuco": "PE", "Piauí": "PI", "Rio de Janeiro": "RJ",
        "Rio Grande do Norte": "RN", "Rio Grande do Sul": "RS", "Rondônia": "RO", "Roraima": "RR",
        "Santa Catarina": "SC", "São Paulo": "SP", "Sergipe": "SE", "Tocantins": "TO"
    }

    for chave, valor in estados.items():
        
        # Montamos o comando para inserção dos dados na tabela
        comando = f"INSERT INTO tb_estados(nome, sigla) VALUES ('{chave}', '{valor}')"

        # Executamos o comando.
        cur.execute(comando)
        print(f"Registro {valor} inserido com sucesso!")

    # Para inserir os dados na tabela, além de executar os commandos INSERT, precisamos "confirmar" a
    # transação utilizando o método commit() do objeto de conexão
    conexao.commit()

    # Listando os dados que foram cadastrados

    comando = "SELECT * FROM tb_estados"
    resultado = cur.execute(comando)

    # O método fetchone() trás apenas o primeiro resultado da consulta
    # Sempre retorna uma tupla com os valores
    print(resultado.fetchone())

    # O método fetchmany(size) trás a quantidade de registros indicados como parâmetro size
    print(resultado.fetchmany(10))

    # O métdo fetchall() trás os registros restantes
    print(resultado.fetchall())

    # Os métodos fetchmany(size) e fetchall() retornam uma lista de tuplas

    # É importante notar que quando utilizamos os métodos fetch, a posição do cursor muda de acordo
    # com o método. Ou seja, se consumirmos todos os registros do objeto cursor, temos que executar
    # o comando de consulta novamente.

    # Trazendo novamente os dados
    resultado = cur.execute(comando)

    estados = resultado.fetchall()

    print("Lista de Estados Brasileiros")

    for estado in estados:
        saida = f"""
        Estado: {estado[1]}
        Sigla: {estado[2]}"""

        print(saida)

    # Últimos comandos a serem executados
    # Remove a tabela tb_estados
    comando = "DROP TABLE tb_estados"
    cur.execute(comando)
    
    # Fecha a conexão do cursor
    cur.close()

    # Fecha a conexão com o banco de dados
    conexao.close()
