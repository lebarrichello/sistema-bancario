def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Deposito: R$ {valor:.2f}")
    else:
        print("Operacao falhou! O valor informado é inválido")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques):
    valor = float(input("Informe o valor do saque: "))

    if valor <= 0:
        print("Operacao falhou! O valor informado é inválido")
    elif valor > saldo:
        print("Operacao falhou! Você não tem saldo suficiente")
    elif valor > limite:
        print("Operacao falhou! O valor do saque excede o limite")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operacao falhou! Número máximo de saques excedido")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print(f"Extrato".center(40, '*'))
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for movimento in extrato:
            print(movimento)
    print(f"\nSaldo: R$ {saldo:.2f}".center(40))
    print("*" * 40)

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=> """

while True:
    opcao = input(menu)
    if opcao == "1":
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == "2":
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques)
    elif opcao == "3":
        exibir_extrato(saldo, extrato)
    elif opcao == "4":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
