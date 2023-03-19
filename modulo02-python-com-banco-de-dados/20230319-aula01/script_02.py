"""
Encapsulamento

É o conceito onde "escondemos" informações internas do objeto, e definimos as "interfaces"
públicas, onde o usuário terá acesso

"""

class ContaBancaria:

    def __init__(self, nome, saldo=0):

        # Criamos 2 atributos privados da classe
        self._nome = nome
        self._saldo = saldo

    def mostrar_saldo(self):
        return self._saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            return valor

        print("Você não possui saldo disponível")    


if __name__ == "__main__":
    
    conta_corrente_viacredi = ContaBancaria("Conta Corrente Viacredi", 1000)

    print(conta_corrente_viacredi.mostrar_saldo())
    conta_corrente_viacredi.depositar(200)
    print(conta_corrente_viacredi.mostrar_saldo())
    conta_corrente_viacredi.sacar(500)
    print(conta_corrente_viacredi.mostrar_saldo())
