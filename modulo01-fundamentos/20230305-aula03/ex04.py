"""
Crie uma função que receba 2 argumentos: base e expoente. Essa função vai retornar o resultado da base elevado ao expoente. Se o valor do expoente não for informado, a função deve considerar que o valor é 2

"""

def ex_04(base, expoente=2):
    return base ** expoente

if __name__ == "__main__":
    
    print(ex_04(4, 3))
    print(ex_04(10))
