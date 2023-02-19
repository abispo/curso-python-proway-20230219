# Cálculo de média de 3 notas

"""
O script irá receber 3 notas via linha de comando. As regras de cálculo
serão as seguintes:

Se a média for menor do que 5, o aluno estará reprovado.
Se a média for maior ou igual a 5 e menor do que 7, o aluno estará de recuperação.
Se a média for maior ou igual a 7, o aluno estará aprovado.
"""

if __name__ == "__main__":

    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3

    if media >= 0 and media <= 10:

        if media < 5:
            print("O aluno foi reprovado com a média {:.2f}.".format(media))

        # elif media < 7    # Também é válido
        elif media >= 5 and media < 7:
            print("O aluno está de recuperação com a média {:.2f}".format(media))

        else:
            print("O aluno foi aprovado com a média {:.2f}".format(media))
    
    else:
        print("A média não está entre 0 e 10")
