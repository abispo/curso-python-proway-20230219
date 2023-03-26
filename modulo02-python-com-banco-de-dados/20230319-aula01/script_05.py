"""
Composição

Composição é quando uma classe compõe ou é composta por outras classes

"""

class Baralho:

    # Implementando o método mágico __len__, podemos passar o objeto dessa classe para a função built-in len()
    def __len__(self):
        return len(self._lista_de_cartas)

    # Quando queremos criar um objeto que seja iterável, precisamos implementar 2 métodos mágicos: __iter__, __next__
    # O método __iter__ por padrão, retorna o próprio objeto
    def __iter__(self):
        return self

    # O método __next__ contém a lógica de iteração da classe
    def __next__(self):
        if self._indice >= len(self._lista_de_cartas):
            raise StopIteration

        carta = self._lista_de_cartas[self._indice]
        self._indice += 1

        return carta

    def __init__(self):

        self._indice = 0

        # Lista que irá armazenar os objetos do tipo Carta
        self._lista_de_cartas = []

        # Lista auxiliar que será usada para criar os objetos do tipo Carta
        self._valores = [
            "2", "3", "4", "5",
            "6", "7", "8", "9",
            "10", "Q", "J", "K", "A"
        ]

        # Lista auxiliar que será usada para criar os objetos do tipo Carta
        self._naipes = [
            "\u2660", "\u2665", "\u2666", "\u2663"
        ]

        # Chama o método para construir o baralho
        self._construir_baralho()


    def _construir_baralho(self):
        for valor in self._valores:
            for naipe in self._naipes:
                self._lista_de_cartas.append(Carta(naipe, valor))


class Carta:
    def __init__(self, naipe, valor):
        self._naipe = naipe
        self._valor = valor


    def __repr__(self):
        return f"Carta {self._valor}{self._naipe}"

    def __str__(self):
        return f"Carta {self._valor}{self._naipe}"


if __name__ == "__main__":

    baralho = Baralho()
    
    print(f"O baralho possui {baralho} cartas")

    for carta in baralho:
        print(carta)
