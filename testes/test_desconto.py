from src.carrinho_compras.desconto import Desconto

def test_desconto_10_porcento():
    d = Desconto(10)
    assert d.aplicar(100.0) == 90.0

def test_desconto_zero_porcento():
    d = Desconto(0)
    assert d.aplicar(100.0) == 100.0

def test_desconto_100_porcento():
    d = Desconto(100)
    assert d.aplicar(100.0) == 0.0

def test_desconto_50_porcento():
    d = Desconto(50)
    assert d.aplicar(200.0) == 100.0

def test_desconto_percentual_guardado():
    d = Desconto(25)
    assert d.percentual == 25