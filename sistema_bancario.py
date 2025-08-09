# ---------- FUNÇÕES DO PROGRAMA ----------

def depositar(saldo, extrato, valor, /):
    if valor > 0:
        saldo += valor
        extrato += f"+ Depósito:   R$   {valor:.2f}\n"
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!\n")
    else:
        print("\nOperação falhou! O valor informado é inválido.\n")
    return saldo, extrato

def sacar(*, saldo, extrato, numero_saques, valor, valor_saque_limite, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > valor_saque_limite
    excedeu_saques = numero_saques >= limite_saques

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

def exibir_extrato(saldo, /, *, extrato):
    print("\n=============== EXTRATO ===============\n")
    print("Nenhuma movimentação realizada." if not extrato else extrato)
    print(f"\nSaldo Atual:  R$   {saldo:.2f}\n")
    print("=======================================\n")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!\n")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("\nUsuário cadastrado com sucesso!\n")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!\n")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado! Cadastro não realizado.\n")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
Agência: {conta['agencia']}
C/C: {conta['numero_conta']}
Titular: {conta['usuario']['nome']}
"""
        print("=" * 30)
        print(linha)


# ---------- PROGRAMA PRINCIPAL ----------

def main():
    AGENCIA = "0001"
    saldo = 0
    valor_saque_limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    menu = """
===============     BANCO     ===============

=============== MENU DE OPÇÕES ==============
    
                [d] Depositar
                [s] Sacar
                [e] Extrato
                [nu] Novo usuário
                [nc] Nova conta
                [lc] Listar contas
                [q] Sair
    
=============================================

==> Escolha uma opção: """

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("\nInforme o valor do depósito: "))
            saldo, extrato = depositar(saldo, extrato, valor)

        elif opcao == "s":
            valor = float(input("\nInforme o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo=saldo, extrato=extrato, numero_saques=numero_saques, valor=valor, valor_saque_limite=valor_saque_limite, limite_saques=LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            cadastrar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("\nObrigado por utilizar nosso sistema bancário! Até logo!\n")
            break

        else:
            print("\nOperação inválida! Por favor, selecione novamente.\n")

if __name__ == "__main__":
    main()