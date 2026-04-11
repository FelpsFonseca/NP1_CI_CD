# NP1_CI_CD 🛒

Projeto acadêmico de **CI/CD** baseado em um **sistema de carrinho de compras** em Python.  
O repositório foi estruturado para demonstrar boas práticas de organização de código, testes automatizados, empacotamento e automação de pipeline ⚙️.

## 🎯 Objetivo

Este projeto tem como objetivo implementar um sistema simples de carrinho de compras, contendo regras básicas de negócio, e integrá-lo a uma esteira de **CI/CD** com:

- execução automática de testes 🧪  
- geração de relatórios 📊  
- build do pacote Python 📦  
- etapa de deploy via webhook 🚀  
- notificação final da execução do pipeline 📢  

---

## ⚙️ Funcionalidades do projeto

O sistema contempla as seguintes entidades e comportamentos:

### Produto 🏷️
Representa um produto com:

- nome  
- preço  

Validações:
- não permite nome vazio  
- não permite preço negativo  

---

### ItemCarrinho 🧾
Representa um item do carrinho, associando:

- produto  
- quantidade  

Validações:
- quantidade deve ser maior que zero  

---

### Carrinho 🛒
Responsável por armazenar e manipular os itens adicionados.

Principais operações:
- adicionar item  
- remover item  
- calcular subtotal  
- calcular total com desconto e frete  
- limpar carrinho  
- contar quantidade total de itens  

Regras implementadas:
- ao adicionar o mesmo produto novamente, a quantidade é somada  
- carrinho vazio retorna total `0`  

---

### Desconto 💸
Aplica desconto percentual sobre um valor.

Regras:
- percentual deve estar entre `0` e `100`  
- não aceita valor negativo para aplicação do desconto  

---

### Frete 🚚
Calcula o valor do frete com base no subtotal.

Regras:
- frete grátis para compras acima de `R$ 200,00`  
- abaixo disso, frete fixo de `R$ 15,00`  

---

### Pedido 📦
Representa um pedido criado a partir de um carrinho.

Estados possíveis:
- `pendente`  
- `confirmado`  
- `cancelado`  
- `entregue`  

Regras:
- não permite criar pedido com carrinho vazio  
- não permite criar pedido com nome de cliente vazio  
- apenas pedidos pendentes podem ser confirmados  
- pedidos entregues não podem ser cancelados  
- só aceita status válidos  

---

## 🗂️ Estrutura do projeto

```bash
NP1_CI_CD/
├── .github/
│   └── workflows/
│       └── pipeline.yml
├── scripts/
│   └── enviar_notificacao.py
├── src/
│   └── carrinho_compras/
│       ├── __init__.py
│       ├── carrinho.py
│       ├── desconto.py
│       ├── frete.py
│       ├── item_carrinho.py
│       ├── pedido.py
│       └── produto.py
├── testes/
│   ├── __init__.py
│   ├── test_carrinho.py
│   ├── test_casos_importunos.py
│   ├── test_desconto.py
│   ├── test_erros_extensao.py
│   ├── test_frete.py
│   ├── test_item_carrinho.py
│   ├── test_pedido.py
│   └── test_produto.py
├── main.py
├── pyproject.toml
├── pytest.ini
├── requirements.txt
├── requirements-dev.txt
└── README.md

```

## 🚀 Tecnologias utilizadas
- 🐍 **Python 3.10+** — linguagem principal do projeto  
- 🌐 **Flask** — criação de uma aplicação web simples  
- 🧪 **Pytest** — framework para testes automatizados  
- 📊 **pytest-html** — geração de relatórios de testes em HTML  
- 📦 **setuptools / wheel / build** — empacotamento da aplicação  
- ⚙️ **GitHub Actions** — automação da pipeline de CI/CD  

## 🧪 Ambiente virtual, dependências e execução

Esta seção mostra como configurar o ambiente do projeto, instalar as dependências e executar a aplicação.

### 🪟 Windows

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
python main.py

```
### 🪟 Linux/macOS
```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
python main.py
```
## 🧪 Como executar os testes

Para executar todos os testes do projeto, utilize o comando abaixo:

```bash
pytest -v
```

### 📊 Relatórios de teste

Durante a execução, podem ser gerados relatórios para análise:

- 📄 Relatório em HTML com detalhes dos testes  
- 📁 Relatório em XML para integração com CI/CD  

### ⚙️ Configuração

O comportamento dos testes é definido no arquivo `pytest.ini`, incluindo:

- 📂 Diretório de testes (`testes`)  
- 📄 Padrão de arquivos (`test_*.py`)  
- 🧱 Classes de teste (`Test*`)  
- 🔧 Funções de teste (`test_*`)

## ⚙️ Pipeline CI/CD

A automação do projeto está configurada no arquivo:

```bash
.github/workflows/pipeline.yml
```

A pipeline é responsável por garantir a qualidade do código, gerar o build e realizar o deploy automaticamente.

### 🔄 Etapas da pipeline

#### 🧪 1. Testes
- Executa os testes automatizados com Pytest  
- Gera relatórios de execução 📊  
- Armazena os resultados como artifacts  

#### 📦 2. Build
- Realiza o empacotamento do projeto  
- Gera os arquivos distribuíveis no diretório `dist/`  

#### 🚀 3. Deploy
- Executa o deploy via webhook 🔗  
- Utiliza variáveis seguras (secrets) para autenticação 🔐  

#### 📢 4. Notificação
- Executa um script de notificação  
- Informa o status final da pipeline (sucesso ou falha)  

## 📦 Empacotamento

O projeto utiliza o arquivo `pyproject.toml` para configuração de empacotamento da aplicação Python.

### ⚙️ Configurações principais

- 📛 Nome do pacote: `carrinho-compras`  
- 🔢 Versão: `1.0.0`  
- 🧾 Descrição do projeto  
- 🐍 Versão mínima do Python: `>=3.10`  
- 📦 Sistema de build baseado em `setuptools`  

---

### 🏗️ Gerar o pacote manualmente

Para criar os arquivos distribuíveis do projeto, execute:

```bash
python -m build
```
Após a execução, os arquivos serão gerados no diretório:

```bash
dist/
```
---

### 📁 Arquivos gerados

- 📦 `.whl` (wheel) — instalação rápida do pacote  
- 📦 `.tar.gz` — distribuição do código fonte  


## ☁️ Deploy Automatizado (Render)

A aplicação está configurada para deploy automático utilizando a plataforma Render.

### 🔗 Funcionamento

* O deploy é acionado automaticamente via *Deploy Hook*
* A chamada é feita a partir da pipeline do GitHub Actions
* O deploy só ocorre se todas as etapas anteriores forem concluídas com sucesso

### ⚙️ Configuração no Render

* Tipo de serviço: Web Service
* Ambiente: Python
* Build Command:


pip install -r requirements.txt


* Start Command:


python main.py


### ⚠️ Porta dinâmica

Para funcionar corretamente no Render, a aplicação utiliza a porta definida pelo ambiente:

python
port = int(os.environ.get("PORT", 10000))


Isso garante compatibilidade com o ambiente de execução da plataforma.

---

## 🔄 Integração com GitHub Actions

O deploy é integrado à pipeline através de uma requisição HTTP:

yaml
- name: Deploy via webhook
  run: curl -X POST ${{ secrets.DEPLOY_HOOK }}


A URL do webhook é armazenada como *Secret* no GitHub, garantindo segurança e evitando exposição de dados sensíveis.

---

## 📢 Notificação do Pipeline

A etapa final da pipeline executa um script Python responsável por informar o status da execução.

* Utiliza variável de ambiente STATUS
* Não utiliza dados hardcoded
* Resultado exibido nos logs do GitHub Actions

Exemplo de saída:

NOTIFICAÇÃO DO PIPELINE
Status final: success
Pipeline executado com sucesso!

## Uso de IA (Claude – Anthropic)

### Pettrius Vilas Boas De Paiva Cardoso

A IA foi utilizada como apoio nas tarefas de build, gerenciamento de dependências, .gitignore e testes de extensão.

**Prompt 1 — Configuração de dependências e build**
> "Configure o `requirements.txt` e `requirements-dev.txt` para o projeto. Crie o `pyproject.toml` necessário para o build funcionar com `python -m build`."

Resultado satisfatório. Os arquivos foram gerados com alguns erros que foi resolvido manualmente, o build foi testado localmente e gerou os pacotes `.tar.gz` e `.whl` sem erros.

---

**Prompt 2 — Job de build no pipeline**
> "Adicione o job de build no `pipeline.yml` existente. O job deve instalar dependências via `requirements-dev.txt`, rodar `python -m build` e salvar o pacote como artifact. Deve executar somente após o sucesso dos testes."

Resultado satisfatório. O job foi criado com `needs: testes` e os steps de instalação, build e upload de artifact.

---

**Prompt 3 — Testes de fluxo de extensão (erro)**
> "Crie 5 testes unitários de fluxo de extensão (erro) que não repitam os testes do outro integrante. Cada teste deve cobrir uma classe diferente do projeto e validar exceções com `pytest.raises`."

Resultado satisfatório. Os 5 testes foram gerados, houve alguns problemas de validação, de forma que correões manuais foram validados localmente - (5/5 passed) e cobrem: `Produto`, `ItemCarrinho`, `Frete`, `Desconto` e `Pedido`.

---

**Prompt 4 — Resolução de conflitos no merge**
> "Resolva os conflitos do rebase entre meu código e o do colega nos arquivos `pipeline.yml`, `.gitignore` e `requirements.txt`, mantendo as alterações de ambos."

Resultado satisfatório. Houve alguns problemas de conflitos de merge, que causavam erros na hora de subir as features e o Claude criou ótimas instruções que resolveram os conflitos, preservando os jobs dos colegas (deploy, notificação) e integrando o job de build e as demais configurações.

## Uso de IA (Claude – Anthropic)

### Pettrius Vilas Boas De Paiva Cardoso

A IA foi utilizada como apoio nas tarefas de build, gerenciamento de dependências, .gitignore e testes de extensão.

*Prompt 1 — Configuração de dependências e build*
> "Configure o requirements.txt e requirements-dev.txt para o projeto. Crie o pyproject.toml necessário para o build funcionar com python -m build."

Resultado satisfatório. Os arquivos foram gerados com alguns erros que foi resolvido manualmente, o build foi testado localmente e gerou os pacotes .tar.gz e .whl sem erros.

---

*Prompt 2 — Job de build no pipeline*
> "Adicione o job de build no pipeline.yml existente. O job deve instalar dependências via requirements-dev.txt, rodar python -m build e salvar o pacote como artifact. Deve executar somente após o sucesso dos testes."

Resultado satisfatório. O job foi criado com needs: testes e os steps de instalação, build e upload de artifact.

---

*Prompt 3 — Testes de fluxo de extensão (erro)*
> "Crie 5 testes unitários de fluxo de extensão (erro) que não repitam os testes do outro integrante. Cada teste deve cobrir uma classe diferente do projeto e validar exceções com pytest.raises."

Resultado satisfatório. Os 5 testes foram gerados, houve alguns problemas de validação, de forma que correões manuais foram validados localmente - (5/5 passed) e cobrem: Produto, ItemCarrinho, Frete, Desconto e Pedido.

---

*Prompt 4 — Resolução de conflitos no merge*
> "Resolva os conflitos do rebase entre meu código e o do colega nos arquivos pipeline.yml, .gitignore e requirements.txt, mantendo as alterações de ambos."

Resultado satisfatório. Houve alguns problemas de conflitos de merge, que causavam erros na hora de subir as features e o Claude criou ótimas instruções que resolveram os conflitos, preservando os jobs dos colegas (deploy, notificação) e integrando o job de build e as demais configurações.

## Uso de IA (ChatGPT – OpenAI)

Felipe Fonseca

A IA foi utilizada como apoio na documentação do projeto, estruturação do README, configuração da pipeline CI/CD e correção de erros no GitHub Actions.

---

### Prompt 1 — Criação do README do projeto

"Analise o repositório e crie um README com as principais informações do projeto."

**Resultado satisfatório.**  
Foi gerado um README completo com estrutura profissional, incluindo descrição do projeto, funcionalidades, estrutura de pastas e instruções de execução. Pequenos ajustes de formatação foram feitos manualmente.

---

## 👨‍💻 Autores

Desenvolvido por **Ana Júlia Pinto, Felipe Fonseca Vidal Prado, Pettrius Vilas Boas de Paiva Cardoso, Vinicius Pereira Cardoso dos Santos**  
🎓 Projeto acadêmico de **CI/CD**

