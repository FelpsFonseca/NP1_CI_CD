class Desconto:
    def __init__(self, percentual: float):
        if percentual < 0 or percentual > 100:
            raise ValueError("Percentual de desconto deve ser entre 0 e 100.")
        self.percentual = percentual

    def aplicar(self, valor: float) -> float:
        if valor < 0:
            raise ValueError("Valor não pode ser negativo.")
        return valor * (1 - self.percentual / 100)