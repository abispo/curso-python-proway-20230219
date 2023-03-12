"""
Escreva uma função que receba uma lista, e retorne a mesma lista, porém sem valores repetidos
"""

def ex03(lista):
    # Podemos utilizar sets para eliminar os valores repetidos da sequência
    return list(set(lista))

if __name__ == "__main__":
    
    lista1 = [1, 1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 9, 9, 9, 9, 10, 10]
    print(ex03(lista1))
