"""
Herança

Herança acontece quando uma classe herda atributos e características de uma classe mãe
ou superclasse

"""

from excecoes import SaldoInsuficienteError

class ContaFinanceira:

    def __init__(self, nome, saldo=0):
        self._nome = nome
        self._saldo = saldo

    def mostrar_saldo(self):
        print(f"O saldo atual da conta '{self._nome}' é de {self._saldo:.2f}")

    def sacar(self):
        raise NotImplementedError

    def depositar(self):
        raise NotImplementedError

    def transferir(self):
        raise NotImplementedError


# Quando queremos indicar a classe a qual será herdada, indicamos o seu nome entre
# parentesis
# No caso abaixo, indicamos que a classe ContaCorrente herda de ContaFinanceira
class ContaCorrente(ContaFinanceira):
    
    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            return valor

        else:
            raise SaldoInsuficienteError


    def depositar(self, valor):
        self._saldo += valor

    # def transferir(self, conta, valor):
    #     conta.depositar(self.sacar(valor))


class ContaInvestimento(ContaFinanceira):

    def __init__(self, nome, saldo=0, taxa=0.01):
        self._taxa = taxa
        super().__init__(nome=nome, saldo=saldo)

    def render(self):
        # self._saldo += (self._saldo * self._taxa)
        self._saldo = self._saldo + (self._saldo * self._taxa)

if __name__ == "__main__":
    
    try:
        conta = ContaCorrente("Teste", 1000)
        conta.sacar(100)

        conta_poupanca = ContaInvestimento("Poupança Caixa", 100)
        conta_poupanca.mostrar_saldo()
        conta_poupanca.render()
        conta_poupanca.mostrar_saldo()

    except Exception as exc:
        print(exc)
