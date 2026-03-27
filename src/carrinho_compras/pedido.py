from src.carrinho_compras.carrinho import Carrinho

class Pedido:
    STATUS_VALIDOS = ["pendente", "confirmado", "cancelado", "entregue"]

    def __init__(self, carrinho: Carrinho, cliente: str):
        if not cliente or not cliente.strip():
            raise ValueError("Nome do cliente não pode ser vazio.")
        if not carrinho.itens:
            raise ValueError("Carrinho não pode estar vazio para criar pedido.")
        self.carrinho = carrinho
        self.cliente = cliente
        self.status = "pendente"

    def confirmar(self):
        if self.status != "pendente":
            raise RuntimeError("Apenas pedidos pendentes podem ser confirmados.")
        self.status = "confirmado"

    def cancelar(self):
        if self.status == "entregue":
            raise RuntimeError("Pedidos entregues não podem ser cancelados.")
        self.status = "cancelado"

    def atualizar_status(self, novo_status: str):
        if novo_status not in self.STATUS_VALIDOS:
            raise ValueError(f"Status inválido: {novo_status}")
        self.status = novo_status