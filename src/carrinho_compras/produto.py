class Produto:
    def __init__(self, nome: str, preco: float):
        if not nome or not nome.strip():
            raise ValueError("Nome do produto não pode ser vazio.")
        if preco < 0:
            raise ValueError("Preço não pode ser negativo.")
        self.nome = nome
        self.preco = preco