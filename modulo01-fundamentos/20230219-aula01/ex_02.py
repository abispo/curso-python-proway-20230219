
if __name__ == "__main__":
    
    produto_1 = float(input("Informe o valor do produto 1: "))
    produto_2 = float(input("Informe o valor do produto 2: "))
    produto_3 = float(input("Informe o valor do produto 3: "))

    soma = produto_1 + produto_2 + produto_3

    if soma < 1000:
        desconto = 0

    elif soma >= 1000 and soma < 5000:
        desconto = 0.1

    elif soma >= 5000 and soma < 10000:
        desconto = 0.2

    else:
        desconto = 0.3

    valor_desconto = soma * desconto
    valor_total = soma - valor_desconto
    
    texto = f"""
    
    O valor total é de R$ {soma:.2f}
    Você ganhou um desconto de {desconto * 100:.2f}%
    O valor total agora é de R$ {valor_total:.2f}
    O valor descontado foi de R$ {valor_desconto:.2f}

    """

    print(texto)