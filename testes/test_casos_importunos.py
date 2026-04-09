import pytest
from src.carrinho_compras.produto import Produto
from src.carrinho_compras.carrinho import Carrinho
from src.carrinho_compras.desconto import Desconto
from src.carrinho_compras.frete import Frete
from src.carrinho_compras.pedido import Pedido

# 1. Produto com preço negativo
def test_produto_preco_negativo():
    with pytest.raises(ValueError):
        Produto("Notebook", -100)

# 2. Adicionar quantidade negativa no carrinho
def test_quantidade_negativa():
    carrinho = Carrinho()
    produto = Produto("Mouse", 50)

    with pytest.raises(ValueError):
        carrinho.adicionar_item(produto, -1)

# 3. Desconto inválido (>100%)
def test_desconto_invalido():
    with pytest.raises(ValueError):
        Desconto(150)

# 4. Carrinho vazio ao calcular total
def test_carrinho_vazio_total():
    carrinho = Carrinho()
    desconto = Desconto(10)
    frete = Frete()

    total = carrinho.total(desconto, frete)
    assert total == 0

# 5. Confirmar pedido sem itens
def test_pedido_sem_itens():
    carrinho = Carrinho()

    with pytest.raises(ValueError):
        Pedido(carrinho, "Cliente")