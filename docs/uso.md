# ▶️ Como usar o sistema

Abaixo está um exemplo básico de utilização do sistema de carrinho de compras:

```python
from carrinho_compras.produto import Produto
from carrinho_compras.item_carrinho import ItemCarrinho
from carrinho_compras.carrinho import Carrinho
from carrinho_compras.desconto import Desconto
from carrinho_compras.frete import Frete
from carrinho_compras.pedido import Pedido

# Criar produtos
produto1 = Produto("Notebook", 3000)
produto2 = Produto("Mouse", 100)

# Criar carrinho
carrinho = Carrinho()

# Adicionar itens ao carrinho
carrinho.adicionar_item(ItemCarrinho(produto1, 1))
carrinho.adicionar_item(ItemCarrinho(produto2, 2))

# Aplicar desconto
desconto = Desconto(10)  # 10%

# Definir frete
frete = Frete()

# Criar pedido
pedido = Pedido("Felipe", carrinho, desconto, frete)

# Confirmar pedido
pedido.confirmar()

# Exibir status do pedido
print(pedido.status)
```

---

## 📌 Fluxo de uso

1. Criar produtos  
2. Adicionar produtos ao carrinho  
3. Aplicar desconto (opcional)  
4. Calcular frete  
5. Criar pedido  
6. Confirmar pedido  

---

## ⚠️ Observações

- Não é possível criar um pedido com carrinho vazio  
- O nome do cliente é obrigatório  
- Descontos devem estar entre 0% e 100%  
- Frete pode ser gratuito dependendo do valor da compra  