"""
Escreva um programa que converta uma lista de inteiros em apenas 1 inteiro. Exemplo:
lista = [4, 7, 10, 24]
Saída: 471024

"""

if __name__ == "__main__":

    lista_numeros = [4, 7, 10, 24]

    texto = ""

    for numero in lista_numeros:
        texto += str(numero)

    print(int(texto))

    # Utilizando list-comprehension
    texto = "".join([str(numero) for numero in [60, 45, 10, 2]])

    print(texto)
