"""
Funções

Parâmetros são valores que podemos passar pra "dentro" das funções
"""

# Definimos os parâmetros dentro dos parêntesis na declaração da função
def calculo_imc(peso, altura):
    return peso / (altura * altura)

# O argumento tipo_funcionário é um argumento com valor padrão.
# Ou seja, se não for infomado um valor para esse parâmetro, ele assume o valor padrão
def calculo_salario(nome, tipo_funcionario=1):
    if tipo_funcionario == 1:
        print(f"O salário de {nome} é 1000")

    else:
        print(f"O salário de {nome} é 2000")

if __name__ == "__main__":

    # Chamamos a função chamando os argumentos de maneira posicional
    imc = calculo_imc(71, 1.78)
    print(imc)

    # Chamamos a função indicando os argumentos pelo nome
    imc = calculo_imc(altura=2.10, peso=121)

    dados_usuario = {
        "peso": 98,
        "altura": 1.79
    }

    print(f"{calculo_imc(**dados_usuario):.2f}")
    # calculo_imc(altura=1.79, peso=90)

    nome = "João"
    calculo_salario(nome, tipo_funcionario=5)