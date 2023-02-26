"""
Escreva um programa que receba números pelo terminal. Se o usuário digitar o número 0, o programa para de receber números pelo terminal e retorna uma lista dos quadrados desses números. Exemplo:
Digite um número: 4
Digite um número: 2
Digite um número: 6
Digite um número: 0

Lista dos quadrados: [16, 4, 36]

"""

if __name__ == "__main__":

    # Criamos uma lista que irá armazenar os quadrados
    lista_numeros = []

    # Aqui o loop irá rodar "infinitamente"
    while True:

        # Recebemos o número informado pelo usuário
        numero = int(input("Digite um número: "))

        # Caso esse número seja 0, interrompemos o loop
        # Basicamente mudamos a condição do loop para dentro dele
        if numero == 0:
            break
         
        # Insermos o valor retornado pela operação de multiplicação na lista
        lista_numeros.append(numero * numero)

    # Imprimimos os valores da lista
    print(lista_numeros)
