"""
Escreva um programa que gere 100 números randômicos de 1 a 100. Em seguida, crie 2 listas: Uma que irá salvar apenas os números pares, e outra que irá salvar apenas os números ímpares. Em seguida, mostre na tela a quantidade de itens de cada lista e quais são os seus valores. Exemplo:
Itens na lista de pares: 5
Valores: [2, 8, 20, 50, 4]

Itens na lista de ímpares: 4
lista_impares = [45, 79, 3]

"""

from random import randint

if __name__ == "__main__":

    # Vamos utilizar a função range() para gerar uma sequência de números de 1 a 100

    numeros_pares = []
    numeros_impares = []

    for _ in range(100):
        
        numero_randomico = randint(1, 100)
        resto = numero_randomico % 2

        if resto == 0:
            numeros_pares.append(numero_randomico)

        else:
            numeros_impares.append(numero_randomico)


    print(f"Itens na lista de pares: {len(numeros_pares)}")
    print(f"Valores: {numeros_pares}")

    print(f"Itens na lista de ímpares: {len(numeros_impares)}")
    print(f"Valores: {numeros_impares}")
