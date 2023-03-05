"""
Escreva um programa em Python que gere uma lista randômica de 50 números de 1 até 50. Em seguida, retire os valores repetidos dessa lista (utilize a função randint() do pacote random)

"""

from random import randint

if __name__ == "__main__":

    lista_randomicos = [randint(1, 50) for _ in range(50)]
    lista_numeros = []

    lista_randomicos.sort()

    for numero in lista_randomicos:
        # Se o número não estiver na lista_numeros, adicione
        if numero not in lista_numeros:
            lista_numeros.append(numero)

    print(lista_randomicos)
    print(lista_numeros)

    # Podemos fazer a mesma coisa utilizando um set, pois esse tipo de
    # dado não permite valores repetidos
    print(list(set(lista_randomicos)))