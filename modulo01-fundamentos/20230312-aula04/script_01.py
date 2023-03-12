"""
Entrada e saída em arquivos txt
I/O (Input/Output)

"""

import os

if __name__ == "__main__":
    """
    Para abrir arquivos em Python, utilizamos a função built-in open()

    A função open() normalmente recebe 2 argumentos: O arquivo a ser aberto, e o modo de abertura
    """
    # os.getcwd() Função do pacote os que retorna o caminho atual de onde o script está sendo executado
    # os.path.join() Função do pacote os que "junta" os caminhos do sistema de arquivos
    # Na linha abaixo, montamos o caminho até o arquivo log.txt que deve estar na mesma pasta que o script
    # está sendo executado

    # A função open retorna um objeto do tipo file
    arquivo = open(os.path.join(os.getcwd(), "log.txt"), "r")

    # Lendo um arquivo utilizando o método read()
    # Podemos passar um valor para o argumento size, que é a quantidade de
    # caracteres que serão lidos

    # Abaixo vamos ler primeiro os 10 primeiros bytes do arquivo
    print(arquivo.read(10))

    # Aqui lemos o arquivo inteiro a partir da posição atual do cursor
    conteudo = arquivo.read()
    print(conteudo)

    # Essa linha não irá imprimir o conteúdo, pois o cursor do arquivo
    # está no final. Para ler novamente o conteúdo, precisamos apontar o cursor
    # pro começo do arquivo
    # O argumento 5 indica a quantidade de bytes que serão lidos na linha atual
    print(arquivo.readline(5))

    # Mostrando a posição atual do cursor
    print(arquivo.tell())

    # Apontar o cursor pro começo do arquivo
    arquivo.seek(0)

    # O método readlines() retorna uma lista contendo as linhas do arquivo
    print(arquivo.readlines())

    # Fecha o arquivo
    arquivo.close()
