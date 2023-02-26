"""
Laços de condição em Python

Laço for

Utilizamos o laço quando queremos iterar (ler de forma sequencial) os itens
de um container (listas, dicts, etc) e objetos iteráveis (string)

Exemplos:
    - Ler o conteúdo de um arquivo texto
    - Acessar os itens de um resultado de uma chamado ao banco de dados
    - etc.

"""

frutas = [
    "Abacaxi", "Manga", "Limão", "Abacate", "Tamarindo"
]

jogos = [
    "CS:GO", "GTA V", "Valorant", "LOL", "Arma 2"
]

if __name__ == "__main__":
    
    for fruta in frutas:
        print(fruta)


    # Uso do break
    # Quando temos o comando break no laço for, o laço é imediatamente
    # interrompido
    for jogo in jogos:
        
        if jogo == "Valorant":
            print("Não roda!")
            break

        print(jogo)

    # Uso do continue
    # Quando temos o comando continue no laço for, a iteração atual é
    # interrompida, e o loop continua no próximo item

    print('='*30)

    for jogo in jogos:

        if jogo == "Valorant":
            print("Não roda, mas roda os outros")
            continue

        print(jogo)

    # O block else em um for loop será executado apenas se não houver um
    # comando break executado dentro do laço for
    else:
        print("Executado com sucesso!")