"""
Crie uma função que receba uma lista de inteiros como argumento. Essa função deve retornar o item que mais aparece na lista e quantas vezes ele aparece
"""

from random import randint

def ex_05(lista):
    dict_numeros = {}

    for numero in lista:

        if dict_numeros.get(numero):
            dict_numeros[numero] += 1

        else:
            dict_numeros[numero] = 1

    print(dict_numeros)

    """
    Salvando o item que mais aparece em uma variável
    """

    maior = 0
    vezes = 0

    for chave, valor in dict_numeros.items():
        if valor >= vezes:
            vezes = valor
            maior = chave

    return maior, vezes


if __name__ == "__main__":
    
    lista = [randint(1, 10) for _ in range(200)]
    mais_aparece, vezes = ex_05(lista)

    print(f"O valor que mais aparece é o {mais_aparece} com {vezes} ocorrências.")
