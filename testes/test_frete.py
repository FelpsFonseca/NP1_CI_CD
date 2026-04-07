from src.carrinho_compras.frete import Frete

def test_frete_cobrado_abaixo_de_200():
    f = Frete()
    assert f.calcular(100.0) == 15.0

def test_frete_gratis_acima_de_200():
    f = Frete()
    assert f.calcular(200.0) == 0.0

def test_frete_gratis_bem_acima_de_200():
    f = Frete()
    assert f.calcular(500.0) == 0.0

def test_frete_valor_exato_limite():
    f = Frete()
    assert f.calcular(199.99) == 15.0

def test_frete_subtotal_zero():
    f = Frete()
    assert f.calcular(0.0) == 15.0