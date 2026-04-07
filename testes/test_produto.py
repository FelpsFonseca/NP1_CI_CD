from src.carrinho_compras.produto import Produto

def test_criar_produto_com_nome_e_preco():
    p = Produto("Notebook", 2500.0)
    assert p.nome == "Notebook"
    assert p.preco == 2500.0

def test_produto_com_preco_zero():
    p = Produto("Brinde", 0.0)
    assert p.preco == 0.0

def test_produto_nome_correto():
    p = Produto("Mouse", 50.0)
    assert p.nome == "Mouse"

def test_produto_preco_float():
    p = Produto("Teclado", 199.99)
    assert p.preco == 199.99

def test_produto_nome_com_espacos():
    p = Produto("HD Externo", 300.0)
    assert p.nome == "HD Externo"