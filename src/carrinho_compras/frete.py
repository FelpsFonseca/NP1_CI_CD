class Frete:
    FRETE_GRATIS_ACIMA = 200.0
    VALOR_FRETE = 15.0

    def calcular(self, subtotal: float) -> float:
        if subtotal < 0:
            raise ValueError("Subtotal não pode ser negativo.")
        if subtotal >= self.FRETE_GRATIS_ACIMA:
            return 0.0
        return self.VALOR_FRETE