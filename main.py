from src.carrinho_compras.produto import Produto
from src.carrinho_compras.carrinho import Carrinho
from src.carrinho_compras.desconto import Desconto
from src.carrinho_compras.frete import Frete
from src.carrinho_compras.pedido import Pedido
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Aplicação CI/CD rodando com sucesso!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    p1 = Produto("Notebook", 2500.00)
    p2 = Produto("Mouse", 80.00)

    carrinho = Carrinho()
    carrinho.adicionar_item(p1, 1)
    carrinho.adicionar_item(p2, 2)

    desconto = Desconto(10)
    frete = Frete()

    total = carrinho.total(desconto, frete)
    print(f"Total do pedido: R$ {total:.2f}")

    pedido = Pedido(carrinho, "João Silva")
    pedido.confirmar()
    print(f"Status do pedido: {pedido.status}")