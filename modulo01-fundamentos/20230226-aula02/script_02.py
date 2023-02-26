"""
Laços de condição em Python

Laço while

O laço while é utilizado quando queremos repetir a execução de um bloco
de código enquanto uma determinada condição é verdadeira.

Exemplos:
    - Execute uma leitura enquanto um valor não for atingido
    - Envio e-mails enquanto uma frase não for lida

"""

if __name__ == "__main__":

    i = 0

    while i < 10:
        print(i)
        i += 1  # i = i + 1

    # Assim como no laço for, podemos ter um comando break dentro do while,
    # que vai encerrar a execução desse loop imediatamente

    while i < 20:

        if i > 15:
            break

        print(i)
        i += 1

    # Também podemos ter o comando continue dentro do while, que passa para a
    # próxima execução do loop

    while i < 40:
        
        if i % 2 == 0:
            print(f"O número {i} é par")
            i += 1
            continue

        print(i)
        i += 1
