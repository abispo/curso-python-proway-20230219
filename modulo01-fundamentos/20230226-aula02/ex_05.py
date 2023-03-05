"""
Escreva um programa que gere números randômicos de 0 até 50. Salve esse números em uma lista. Em seguida, informe quais são o maior e o menor número dessa lista. Dica: Utilize as funções built-in max() e min()
"""

from random import randint

if __name__ == "__main__":

    # Utilizando list comprehension
    lista_numeros = [randint(0, 50) for _ in range(50)]

    """
    # Caso não queiramos utilizar o valor gerado pela função range
    # Podemos utilizar o _ (underline) para ignorar esse valor
    lista_numeros = []

    for _ in range(50):
        lista_numeros.append(randint(0, 50))
    """

    print(f"O maior número dessa lista é o {max(lista_numeros)}.")
    print(f"O menor número dessa lista é o {min(lista_numeros)}.")
