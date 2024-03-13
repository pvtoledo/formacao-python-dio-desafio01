menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Qual o valor será depositado? \n"))

        if deposito >= 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print("Valor depositado com sucesso.")
        else:
            print("Operação não realizada! Valor informado é inválido.")
    elif opcao == "s":
        saque = float(input("Qual o valor será sacado? \n"))

        maior_que_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques > LIMITE_SAQUES

        if maior_que_saldo:
            print("Operação não realizada! Saldo insuficiente!")
        elif excedeu_limite:
            print("Operação não realizada! Valor solicitado ultrapassa o limite de saque.")
        elif excedeu_saques:
            print("Operação não realizada! Número máximo de saques excedido.")
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
            print("Valor sacado com sucesso.")
        else:
            print("Operação não realizada! Valor informado é inválido.")
    elif opcao == "e":
        print("\n===================Extrato=====================")
        print("Nenhuma operação realizada." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n===============================================")

    elif opcao == "q":
        break

    else:
        print("opção inválida! Digite novamente.")
