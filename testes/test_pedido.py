from src.carrinho_compras.carrinho import Carrinho
from src.carrinho_compras.produto import Produto
from src.carrinho_compras.pedido import Pedido

def test_criar_pedido():
    c = Carrinho()
    c.adicionar_item(Produto("Livro", 30.0))
    p = Pedido(c, "Julia")
    assert p.status == "pendente"

def test_confirmar_pedido():
    c = Carrinho()
    c.adicionar_item(Produto("Livro", 30.0))
    p = Pedido(c, "Julia")
    p.confirmar()
    assert p.status == "confirmado"

def test_cancelar_pedido():
    c = Carrinho()
    c.adicionar_item(Produto("Livro", 30.0))
    p = Pedido(c, "Julia")
    p.cancelar()
    assert p.status == "cancelado"

def test_cliente_no_pedido():
    c = Carrinho()
    c.adicionar_item(Produto("Livro", 30.0))
    p = Pedido(c, "Julia")
    assert p.cliente == "Julia"

def test_atualizar_status_pedido():
    c = Carrinho()
    c.adicionar_item(Produto("Livro", 30.0))
    p = Pedido(c, "Julia")
    p.atualizar_status("entregue")
    assert p.status == "entregue"