"""
Escreva uma função em Python que informe uma quantidade arbitrária de argumentos do tipo inteiro, e retorne a soma desses valores.

"""


def ex01(*args):
    return sum(args)

if __name__ == "__main__":
    
    print(ex01())
    print(ex01(2, 4, 5))
    print(ex01(1, 2, 3, 4, 5))
