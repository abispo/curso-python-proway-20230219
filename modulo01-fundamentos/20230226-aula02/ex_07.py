"""
Escreva um programa que receba nome, idade e sexo de 5 usuários. Em seguida, mostre quantos usuários são do sexo masculino, quantos são do sexo feminino e qual é a média de idade. Exemplo:
Nome: João
Idade: 32
Sexo: M

Nome: Maria
Idade: 17
Sexo: F

Nome: Vanessa
Idade: 28
Sexo: 7

Quantidade de usuários do sexo masculino: 1
Quantidade de usuários do sexo feminino: 2
Média de idade: 25.67
"""

if __name__ == "__main__":
    
    # Criar a lista que irá armazenar as informações
    lista_clientes = []
    qtd_sexo_masculino = 0
    qtd_sexo_feminino = 0
    soma_idades = 0

    # Loop que roda 5 vezes
    for _ in range(5):
        
        nome = input("Informe o nome: ")
        idade = int(input("Informe a idade: "))
        sexo = input("Informe o sexo: ")

        soma_idades = soma_idades + idade

        if sexo.upper() == "M":
            qtd_sexo_masculino = qtd_sexo_masculino + 1

        else:
            qtd_sexo_feminino = qtd_sexo_feminino + 1

        info = {
            # chave: valor
            "nome": nome,
            "idade": idade,
            "sexo": sexo
        }

        lista_clientes.append(info)

    for cliente in lista_clientes:
        print(f"Nome: {cliente['nome']}")
        print(f"Idade: {cliente['idade']}")
        print(f"Sexo: {cliente.get('sexo')}\n")

    print(f"Quantidade de usuários do sexo masculino: {qtd_sexo_masculino}.")
    print(f"Quantidade de usuários do sexo feminino: {qtd_sexo_feminino}.")
    print(f"Média de idade: {soma_idades / len(lista_clientes):.2f}")