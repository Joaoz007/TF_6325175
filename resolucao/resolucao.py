
from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    @abstractmethod
    def pagar(self, pedido): 
        pass

class Notificador(ABC):
    @abstractmethod
    def notificar(self, pedido):
        pass

class PagamentoCartaoCredito(MetodoPagamento):
    def pagar(self, pedido):
        print(f"Pagando R$ {pedido['valor']:.2f} com cartão de crédito...")

class PagamentoBoleto(MetodoPagamento):
    def pagar(self, pedido):
        print(f"Gerando boleto no valor de R$ {pedido['valor']:.2f}...")

class PagamentoPix(MetodoPagamento):
    def pagar(self, pedido):
        print(f"Pagando R$ {pedido['valor']:.2f} via Pix...")

class NotificacaoEmail(Notificador):
    def notificar(self, pedido):
        print(f"Enviando e-mail de confirmação para {pedido['cliente_email']}...")

class NotificacaoSMS(Notificador):
    def notificar(self, pedido):
        print(f"Enviando SMS de confirmação para {pedido['cliente_telefone']}...")

class ProcessadorDePedidos:
    def __init__(self, metodo_pagamento: MetodoPagamento, notificador: Notificador):
        self.metodo_pagamento = metodo_pagamento
        self.notificador = notificador

    def processar(self, pedido):
        print(f"Processando o pedido #{pedido['id']} no valor de R$ {pedido['valor']:.2f}...")
        self.metodo_pagamento.pagar(pedido)
        self.notificador.notificar(pedido)
        pedido['status'] = 'concluido'
        print("Pedido concluído!")