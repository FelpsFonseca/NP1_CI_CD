from src.carrinho_compras.carrinho import Carrinho
from src.carrinho_compras.produto import Produto

def test_adicionar_item():
    c = Carrinho()
    p = Produto("Livro", 30.0)
    c.adicionar_item(p, 1)
    assert c.quantidade_itens() == 1

def test_subtotal_carrinho():
    c = Carrinho()
    c.adicionar_item(Produto("Livro", 30.0), 2)
    assert c.subtotal() == 60.0

def test_remover_item():
    c = Carrinho()
    p = Produto("Livro", 30.0)
    c.adicionar_item(p)
    c.remover_item("Livro")
    assert c.quantidade_itens() == 0

def test_limpar_carrinho():
    c = Carrinho()
    c.adicionar_item(Produto("Livro", 30.0))
    c.limpar()
    assert c.quantidade_itens() == 0

def test_adicionar_mesmo_produto_aumenta_quantidade():
    c = Carrinho()
    p = Produto("Livro", 30.0)
    c.adicionar_item(p, 1)
    c.adicionar_item(p, 2)
    assert c.quantidade_itens() == 3