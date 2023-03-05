"""
Dicionários

Dicionários são estruturas que armazenam dados no formato chave-valor.
Dicionários são indexáveis, iteráveis, modificáveis e que não permitem
chaves duplicadas.
"""

if __name__ == "__main__":

    # Podemos criar dicionários de 2 maneiras: Diretamente e utilizando
    # a função built-in dict()

    # Forma direta
    cliente = {
        "nome": "Maria",
        "idade": 30,
        "status": "Inativa"
    }

    # Utilizando a função built-in dict()
    # Os parâmetros da função serão as chaves, e os valores serão
    # associados às chaves
    cliente = dict(nome="José", idade=28, status="Ativo")

    print(cliente)

    # Como os dicionários são indexáveis, utilizamos o nome da chave
    # pra acessar o seu valor
    print(cliente["idade"])

    # Os dicionários também são iteráveis, ou seja, conseguimos acessar
    # os itens de maneira sequencial

    # Quando chamamos dessa maneira, o método keys() é chamado
    # de forma indireta
    for item in cliente:
        print(item)

    # Se quisermos pegar tanto chave quanto valor do dicionário, 
    # temos que utilizar o método items()
    for chave, valor in cliente.items():
        print(chave)
        print(valor)

    # Ao criar um dicionário baseado em um já existente, temos o mesmo
    # problema de cópia de listas.
    # Precisamos utilizar o método copy() para criar uma cópia do
    # dicionário é salvar em outro
    dict2 = cliente.copy()
    dict2["status"] = "Inativo"

    print(cliente)
    print(dict2)