"""
Funções com argumentos arbitrários

*args
**kwargs
"""

def calculo_media_arbitrario(*args):
    print(f"{sum(args) / len(args):.2f}")

# kw = keyword
def info_usuario(**kwargs):
    print(kwargs)


if __name__ == "__main__":
    
    # calculo_media_arbitrario()
    # calculo_media_arbitrario(4, 6, "q3q", [1, 5, 7], {"ssf": 1}, 1, 2)
    calculo_media_arbitrario(4, 7, 6)

    info_usuario(nome="João", idade=30)
    info_usuario(nome="João", data_nascimento="19970605", sexo="M", cidade="Blumenau")