"""
Polimorfismo

Polimorfismo significa "muitas formas", ou seja, uma função ou método que pode ser
chamado de diferentes maneiras ou possui diferentes comportamentos.

"""

class Funcionario:
    
    def __init__(self, nome):
        self._nome = nome

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def get_nome(self):
        return self._nome


    # O decorator property faz um método se comportar como um atributo
    # No caso abaixo, essa é a maneira de se criar um 'getter' em python
    @property
    def nome(self):
        return self._nome

    # O código abaixo define um setter para o atributo _nome
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome


    def calcular_salario(self):
        # A linha abaixo força as classes filhas a implementarem esse método
        raise NotImplementedError

class FuncionarioCLT(Funcionario):
    
        def __init__(self, nome, salario):
            self._salario = salario
            super().__init__(nome)


        def calcular_salario(self):
             return self._salario


class FuncionarioTerceirizado(Funcionario):
    
        def __init__(self, nome, valor_hora, qtd_horas):
            self._valor_hora = valor_hora
            self._qtd_horas = qtd_horas
            super().__init__(nome)


        def calcular_salario(self):
             return self._qtd_horas * self._valor_hora


class FuncionarioComissionado(Funcionario):
    
        def __init__(self, nome, valor_vendas, porcentagem_comissao):
            self._valor_vendas = valor_vendas
            self._porcentagem_comissao = porcentagem_comissao
            super().__init__(nome)


        def calcular_salario(self):
             return self._valor_vendas * (self._porcentagem_comissao / 100)

if __name__ == "__main__":
    
    joao = FuncionarioCLT("João", 2000)
    maria = FuncionarioTerceirizado("Maria", 80, 160)
    jose = FuncionarioComissionado("José", 100000, 5)

    for funcionario in [joao, maria, jose]:
        print(f"O funcionário {funcionario.nome} recebeu {funcionario.calcular_salario():.2f}")
