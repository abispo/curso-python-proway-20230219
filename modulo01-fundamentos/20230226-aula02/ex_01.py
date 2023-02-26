"""
Escreva um programa que receba um número maior do que 1 pelo terminal. Em seguida, o programa retorna a soma de 1 até esse número. Ex:

Informe o número: 5
A soma de 1 até 5 é 15

"""

if __name__ == "__main__":
    
    numero = int(input("Informe o número: "))
    soma = 0
    contador = 1

    if numero <= 1:
        print("Você precisa informar um número maior do que 1")
    
    else:
        while contador <= numero:
            soma = soma + contador
            contador += 1

        print(soma)
