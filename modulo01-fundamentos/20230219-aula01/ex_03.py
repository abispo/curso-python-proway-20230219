
if __name__ == "__main__":

    nota_1 = float(input("Informe a primeira nota: "))
    nota_2 = float(input("Informe a segunda nota: "))
    nota_3 = float(input("Informe a terceira nota: "))
    nota_4 = float(input("Informe a quarta nota: "))
    nota_5 = float(input("Informe a quinta nota: "))

    """
    Podemos criar listas de 2 maneiras:

    lista = list()
    lista = []

    """
    # O método append insere um item sempre no final da lista
    # lista_notas.append(nota_1)
    # lista_notas.append(nota_2)

    # Também podemos criar uma lista já com os valores
    lista_notas = [
        nota_1, nota_2, nota_3, nota_4, nota_5
    ]

    lista_notas.sort()

    # Podemos remover o menor e o maior valor das seguintes maneiras
    # Utilizando o método pop()

    # lista_notas.pop(0)
    # lista_notas.pop(-1)

    # Podemos também fazer o fatiamento (slice) da lista, onde passamos
    # um índice inicial e um índice final dos valores que queremos extrair.
    # Nesse caso é gerada uma nova lista
    lista_nova = lista_notas[1:4]

    # len() é uma função built-in que retorna a quantidade de itens de um
    # iterator (no nosso caso, a lista de notas)
    # sum() é outra função built-in que retorna a soma dos números em um 
    # container (no nosso caso, uma lista)
    media = sum(lista_nova) / len(lista_nova)

    print(f"Média: {media:.2f}")
