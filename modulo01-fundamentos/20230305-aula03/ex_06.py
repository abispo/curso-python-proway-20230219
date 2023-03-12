"""
Crie uma função que calcule a média de valores informados. A função receberá uma lista com 5 valores, e pra calcular a média vai ignorar o maior e o menor valor.
"""

def ex06(notas):
    notas.sort()

    return sum(notas[1:4]) / len(notas[1:4])

if __name__ == "__main__":
    
    print(f"{ex06([7.5, 8.5, 7, 7, 10]):.2f}")