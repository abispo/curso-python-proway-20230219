"""
Funções (Procedures)

Função é um bloco de código que pode ser reutilizado em quaisquer lugares
do nosso código.

Em Python, utilizamos a palavra reservada def para criar funções
"""

def hello():
    print("Olá")


def randomico():
    return 1

if __name__ == "__main__":
    
    # Para executar a função, simplesmente a chamamos
    # Funções são objetos chamáveis (callable)
    # Como não utilizamos a instrução return dentro da função hello,
    # por padrão, essa função vai retornar um valor None
    print(hello())

    # Nesse caso, a função randomico() retorna um valor
    # que é salvo em uma variável
    valor = randomico()
    print(valor)
