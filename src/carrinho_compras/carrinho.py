from src.carrinho_compras.item_carrinho import ItemCarrinho
from src.carrinho_compras.produto import Produto
from src.carrinho_compras.desconto import Desconto
from src.carrinho_compras.frete import Frete

class Carrinho:
    def __init__(self):
        self.itens: list[ItemCarrinho] = []

    def adicionar_item(self, produto: Produto, quantidade: int = 1):
        for item in self.itens:
            if item.produto.nome == produto.nome:
                item.quantidade += quantidade
                return
        self.itens.append(ItemCarrinho(produto, quantidade))

    def remover_item(self, nome_produto: str):
        for item in self.itens:
            if item.produto.nome == nome_produto:
                self.itens.remove(item)
                return
        raise ValueError(f"Produto '{nome_produto}' não encontrado no carrinho.")

    def subtotal(self) -> float:
        return sum(item.subtotal() for item in self.itens)

    def total(self, desconto: Desconto = None, frete: Frete = None) -> float:
        valor = self.subtotal()
        if desconto:
            valor = desconto.aplicar(valor)
        if frete:
            valor += frete.calcular(self.subtotal())
        if not self.itens:
            return 0
        return valor

    def limpar(self):
        self.itens = []

    def quantidade_itens(self) -> int:
        return sum(item.quantidade for item in self.itens)