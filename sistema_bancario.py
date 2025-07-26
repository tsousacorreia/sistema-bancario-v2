# ---------- FUNÇÕES DO PROGRAMA ----------

def depositar(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato += f"+ Depósito:   R$   {valor:.2f}\n"
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!\n")
    else:
        print("\nOperação falhou! O valor informado é inválido.\n")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, valor, valor_saque_limite, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > valor_saque_limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("\nOperação falhou! Saldo insuficiente.\n")
    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.\n")
    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.\n")
    elif valor > 0:
        saldo -= valor
        extrato += f"- Saque:      R$   {valor:.2f}\n"
        numero_saques += 1
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!\n")
    else:
        print("\nOperação falhou! O valor informado é inválido.\n")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n=============== EXTRATO ===============\n")
    print("Nenhuma movimentação realizada." if not extrato else extrato)
    print(f"\nSaldo Atual:  R$   {saldo:.2f}\n")
    print("=======================================\n")


# ---------- PROGRAMA PRINCIPAL ----------

menu = """
===============     BANCO     ===============

=============== MENU DE OPÇÕES ==============

                [d] Depositar
                [s] Sacar
                [e] Extrato
                [q] Sair

=============================================

==> Escolha uma opção: """

saldo = 0
valor_saque_limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("\nInforme o valor do depósito: "))
        saldo, extrato = depositar(saldo, extrato, valor)

    elif opcao == "s":
        valor = float(input("\nInforme o valor do saque: "))
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, valor, valor_saque_limite, LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "q":
        print("\nObrigado por utilizar nosso sistema bancário! Até logo!\n")
        break

    else:
        print("\nOperação inválida! Por favor, selecione novamente.\n")