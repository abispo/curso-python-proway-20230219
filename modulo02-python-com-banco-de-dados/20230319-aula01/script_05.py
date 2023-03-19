"""
Composição

Composição é quando uma classe compõe ou é composta por outras classes

"""

class Baralho:

    def __init__(self):

        self._valores = [
            "2", "3", "4", "5",
            "6", "7", "8", "9",
            "10", "Q", "J", "K", "A"
        ]

        self._naipes = [
            "\u2660", "\u2665", "\u2666", "\u2663"
        ]


class Carta:
    def __init__(self, naipe, valor):
        self._naipe = naipe
        self._valor = valor