"""
Escreva uma função em Python que receba 3 parâmetros: inicio, fim e numero. A função deve retornar True se o numero estiver entre inicio e fim
"""

def ex02(inicio, fim, numero):
    return inicio < numero < fim


if __name__ == "__main__":
    
    print(ex02(10, 2, 3))
    print(ex02(2, 8, 4))
