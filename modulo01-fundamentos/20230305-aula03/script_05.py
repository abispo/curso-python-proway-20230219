"""
Funções lambda

Funções lambda são funções que não possuem nome. Utilizamos a palavra reservada lambda.
"""

from random import randint

def quadrado(numero):
    return numero * numero


if __name__ == "__main__":

    # Criar uma lista de números randômicos utilizando list-comprehension
    lista_randomicos = [randint(1, 100) for _ in range(100)]

    """
    O código acima é a mesma coisa que fazer o seguinte:
    lista_randomicos = []
    for _ in range(100):
        lista_randomicos.append(randint(1, 100))
    """

    nova_lista = []

    for numero in lista_randomicos:
        nova_lista.append(quadrado(numero))

    print("Lista de quadrados utilizando a função quadrado()")
    print(nova_lista)

    # Criar uma função anônima (lambda) que retorna o quadrado do argumento x
    # A função map() recebe 2 argumentos: A função que será aplicada a cada item da
    # sequência, e a sequência em si
    # No caso abaixo, a função map vai multiplicar cada item da sequência por ele mesmo
    nova_lista = list(map(lambda x: x * x, lista_randomicos))

    print("Lista de quadrados utilizando map() e lambda")
    print(nova_lista)

    # Criar uma lista apenas com os números pares da nova_lista
    # A função filter aplica uma função para cada item da sequência.
    # Caso essa função retorne o valor booleano True, o valor dessa lista é retornado
    nova_lista_pares = list(filter(lambda x: x % 2 == 0, nova_lista))

    # Lista de pares utilizando a função filter()
    print(nova_lista_pares)
