
class SaldoInsuficienteError(Exception):

    def __init__(self, mensagem = "Não há saldo suficiente na conta"):
        super().__init__(mensagem)


class OperacaoNaoPermitida(Exception):
    def __init__(self, mensagem = ""):
        super().__init__(f"Operação não permitida: {mensagem}")
