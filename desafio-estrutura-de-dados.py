def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(menu)


'''
Parametros em funções:
- *: Significa que aceita apenas parâmetros nomeados (keywords)
- /: Significa que aceita apenas parâmetros posicionais (positional)
Quando não estiver informado, aceita de qualquer uma das formas.
'''


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso!")
    else:
        print("\n Operação não realizada! O valor informado é inválido.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    maior_que_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if maior_que_saldo:
        print("Operação não realizada! Saldo insuficiente!")
    elif excedeu_limite:
        print("Operação não realizada! Valor solicitado ultrapassa o limite de saque.")
    elif excedeu_saques:
        print("Operação não realizada! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Valor sacado com sucesso.")
    else:
        print("Operação não realizada! Valor informado é inválido.")

    return saldo, extrato, numero_saques


def imprimir_extrato(saldo, /, *, extrato):
    print("\n===================Extrato=====================")
    print("Nenhuma operação realizada." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n===============================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF do usuário: \n")
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("CPF já cadastrado anteriormente!\n")
            return
    nome = input("Digite o nome do usuário:\n")
    data_nascimento = input("Digite a data de nascimento do usuário:\n")
    endereco = input("Digite o endereço do usuário: \n")

    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})

    print("Usuário cadastrado com sucesso! \n")


def criar_conta(contas, usuarios, agencia):
    numero_conta = len(contas) + 1
    cpf = input("Informe o CPF do titular da conta: \n")
    for u in usuarios:
        if u["cpf"] == cpf:
            usuario = u
    if usuario:
        print("Conta criada com sucesso! \n")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário não encontrado! Tente novamente.")


def listar_contas(contas):
    for conta in contas:
        linha = f"Agência: {conta['agencia']} \n C/C: {conta['numero_conta']} \n Titular: {conta['usuario']['nome']} \n"
        print("=" * 50)
        print(linha)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "q":
            break
        elif opcao == "d":
            valor = float(input("Qual o valor a ser depositado? "))

            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Qual o valor a ser sacado? \n"))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
        elif opcao == "e":
            imprimir_extrato(saldo, extrato=extrato)
        elif opcao == 'nu':
            criar_usuario(usuarios)
        elif opcao == 'nc':
            conta = criar_conta(contas, usuarios, AGENCIA)
            if conta:
                contas.append(conta)
        elif opcao == 'lc':
            listar_contas(contas)


main()
