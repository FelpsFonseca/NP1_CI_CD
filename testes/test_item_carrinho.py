from src.carrinho_compras.item_carrinho import ItemCarrinho
from src.carrinho_compras.produto import Produto

def test_subtotal_item():
    p = Produto("Caneta", 2.0)
    item = ItemCarrinho(p, 3)
    assert item.subtotal() == 6.0

def test_quantidade_item():
    p = Produto("Caderno", 10.0)
    item = ItemCarrinho(p, 5)
    assert item.quantidade == 5

def test_produto_no_item():
    p = Produto("Régua", 1.5)
    item = ItemCarrinho(p, 1)
    assert item.produto.nome == "Régua"

def test_subtotal_quantidade_um():
    p = Produto("Borracha", 3.0)
    item = ItemCarrinho(p, 1)
    assert item.subtotal() == 3.0

def test_subtotal_preco_float():
    p = Produto("Lápis", 1.5)
    item = ItemCarrinho(p, 4)
    assert item.subtotal() == 6.0