"""
Entrada e saída em arquivos txt
I/O (Input/Output)

Escrita de arquivos

"""

import os

if __name__ == "__main__":
    
    # Utilizamos a palavra reservada with para criar um contexto dentro do nosso código
    # A vantagem de se utilizar with é que o arquivo é fechado automaticamente quando saímos do bloco.
    # Quando abrimos o arquivo no modo "w", se o arquivo não existir, ele é criado
    # Caso o arquivo já exista, seu conteúdo é sobrescrito.
    with open(os.path.join(os.getcwd(), "texto_02.txt"), "w") as arquivo:
        
        nome = input("Informe o seu nome: ")

        # O método write escreve uma string no arquivo
        arquivo.write(f"Seja bem vindo ao curso de Python, {nome}!")

        # O método writelines recebe uma lista de valores e insere no arquivo
        arquivo.writelines(["Python\n", "Golang\n", "Java\n", "PHP\n"])

    # Quando abrimos o arquivo no modo a (append), se o arquivo não existir, ele é criado
    # Caso o arquivo exista, o cursor é enviado para o final do arquivo, com isso sendo possível
    # adicionar mais informações no arquivo
    with open(os.path.join(os.getcwd(), "texto_02.txt"), "a", encoding="utf-8") as arquivo:

        arquivo.write("Esse texto não sobrescreveu o arquivo")

    # Também podemos abrir o arquivo ao mesmo tempo como leitura e escrita
    with open(os.path.join(os.getcwd(), "texto_02.txt"), "r+") as arquivo:
        print(arquivo.read())