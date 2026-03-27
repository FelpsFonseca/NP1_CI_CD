from src.carrinho_compras.produto import Produto

class ItemCarrinho:
    def __init__(self, produto: Produto, quantidade: int):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero.")
        self.produto = produto
        self.quantidade = quantidade

    def subtotal(self) -> float:
        return self.produto.preco * self.quantidade