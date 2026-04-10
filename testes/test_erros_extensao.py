import pytest
from src.carrinho_compras.produto import Produto
from src.carrinho_compras.item_carrinho import ItemCarrinho
from src.carrinho_compras.carrinho import Carrinho
from src.carrinho_compras.desconto import Desconto
from src.carrinho_compras.frete import Frete
from src.carrinho_compras.pedido import Pedido


def test_produto_nome_vazio():
    """Produto não pode ter nome vazio."""
    with pytest.raises(ValueError):
        Produto("", 50.0)


def test_item_carrinho_quantidade_zero():
    """ItemCarrinho não aceita quantidade zero."""
    p = Produto("Caneta", 2.0)
    with pytest.raises(ValueError):
        ItemCarrinho(p, 0)


def test_frete_subtotal_negativo():
    """Frete não pode ser calculado com subtotal negativo."""
    f = Frete()
    with pytest.raises(ValueError):
        f.calcular(-50.0)


def test_desconto_aplicar_valor_negativo():
    """Desconto não pode ser aplicado sobre valor negativo."""
    d = Desconto(10)
    with pytest.raises(ValueError):
        d.aplicar(-100.0)


def test_pedido_cancelar_entregue():
    """Pedido entregue não pode ser cancelado."""
    c = Carrinho()
    c.adicionar_item(Produto("Livro", 30.0))
    p = Pedido(c, "Julia")
    p.atualizar_status("entregue")
    with pytest.raises(RuntimeError):
        p.cancelar()