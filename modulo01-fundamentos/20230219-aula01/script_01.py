# Entrada e saída em Python no terminal

# Isso é um comentário

# A linha abaixo indica que esse script será chamado primeiro na nossa aplicação
# Apesar de não ser obrigário, é considerada uma boa prática.
if __name__ == "__main__":

    # A função print recebe um tipo de dado (string, numero, objeto, etc) e
    # exibe no terminal
    print("Olá mundo.")

    # A função input espera uma informação ser digitada pelo teclado e retorna
    # esse valor
    # A função input() pode receber um argumento não obrigatório prompt, que será
    # o texto a ser exibido para o usuário
    nome = input("Informe o seu nome: ")

    # A função input retorna uma string com a informação que veio do teclado.
    print("Bem vindo " + nome)

    # String é o tipo de dado em Python que representa uma cadeia de caracteres.
    # É considerada string qualquer coisa que estiver dentro de aspas duplas ("")
    # ou aspas simples ('')

    numero1 = int(input("Informe o primeiro número: "))
    numero2 = input("Informe o segundo número: ")

    soma = numero1 + int(numero2)

    # f-strings são strings onde podemos substituir os valores que estão dentro de chaves
    # por qualquer expressão válida em Python
    print(f"A soma dos valores {numero1} e {numero2} é igual a {soma}")

    # Expressões em Python são conjuntos de operadores e operandos que resolvem para
    # um único valor
    numero3 = 8 + (3 ** 3) / 5 - (14* 5) + 0
    print(numero3)

    