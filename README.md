# Sistema Bancário - Versão 2 (Lab Project)

## Descrição:
Lab Project "Criando um sistema bancário com Python" do **Bootcamp Santander 2025 - Back-End com Python**.
O sistema simula operações bancárias básicas (depósito, saque e extrato) de forma simples e funcional, utilizando Programação Orientada a Objetos (POO).

---

## Novas Funcionalidades (Versão 3):
- Cadastrar cliente: Registro de pessoa física com nome, CPF, data de nascimento e endereço; Evita cadastros duplicados pelo CPF.
- Criar conta corrente: Cada conta é associada a um cliente já existente; Criada com limite de saque e limite de número de saques diários.
- Depositar: Permite adicionar saldo à conta do cliente; Valor deve ser positivo.
- Sacar: Permite retirar saldo da conta respeitando: Limite diário de saques; Limite máximo por saque; Saldo disponível.
- Exibir extrato: Lista todas as transações da conta, com tipo, valor e data/hora; Exibe o saldo final; Mensagem informativa caso não haja transações.
- Listar contas: Mostra as informações de todas as contas cadastradas.
- Menu interativo: Interface no terminal com opções para todas as operações.

## Funcionalidades (Versão 2):

- Cadastro de clientes (com CPF, nome, data de nascimento e endereço)
- Cadastro de múltiplas contas correntes por cliente
- Listagem de clientes cadastrados
- Listagem de contas existentes
- Associação automática de novas contas ao cliente existente
- Estrutura modularizada para facilitar manutenção e expansão

## Funcionalidades (Versão 1):

- Depósito de valores positivos
- Saques limitados a R$ 500,00 e até 3 saques diários
- Registro de todas as transações no extrato
- Exibição de extrato formatado com saldo atualizado
- Mensagens amigáveis para o usuário

---

## Tecnologias Utilizadas:
- **Python 3.12.3**
- **PyCharm** (IDE utilizada no desenvolvimento)

---

## Estrutura do Projeto:
sistema-bancario-v1/

├── sistema_bancario.py # Código principal

└── README.md # Documentação do projeto