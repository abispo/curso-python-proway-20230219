"""
Desenvolver um script de cálculo de comissão de vendas.

Regras:

O vendedor terá um salário fixo de R$ 1000,00. Dependendo do valor vendido no mês, o funcionário
receberá uma comissão de x%. Esse valor vendido será recebido pelo terminal. Regras:

Se o funcionário vendeu menos de R$ 10000,00, não recebe comissão
Se o funcionário vendeu entre R$ 10000,00 e menos que R$ 50000,00, receberá 10% de comissão
Se o funcionário vendeu entre R$ 50000,00 e menos que R$ 200000,00, receberá 20% de comissão
Se o funcionário vendeu igual ou acima de R$ 200000,00, receberá 30% de comissão

No final, será mostrado o valor fixo + comissão

"""


if __name__ == "__main__":

    SALARIO_FIXO = 1000
    valor_final = 0

    valor_vendas = float(input("Informe o valor de vendas do funcionário: "))

    # Aqui foi ignorada a comparação de valor_vendas < 10000, pois como definimos o valor da
    # comissao como 0, se o valor de vendas for menor do que 10000, consideramos a comissao como 0

    if valor_vendas >= 10000 and valor_vendas < 50000:
        comissao = valor_vendas * 0.1

    elif valor_vendas >= 50000 and valor_vendas < 200000:
        comissao = valor_vendas * 0.2

    elif valor_vendas >= 200000:
        comissao = valor_vendas * 0.3

    valor_final = SALARIO_FIXO + comissao

    texto = f"""
    Salário Fixo: R$ {SALARIO_FIXO:.2f}
    Valor de vendas: R$ {valor_vendas:.2f}
    Valor da comissão: R$ {comissao:.2f}

    Valor final: R$ {valor_final:.2f}
    
    """

    print(texto)
