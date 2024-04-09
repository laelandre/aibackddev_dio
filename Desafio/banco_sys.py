menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair


=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        adiciona = float(input("Qual o valor do deposito: "))
        if adiciona > 0:
            saldo += adiciona
            print(saldo)
            extrato += f"Depósito: R$ {adiciona:.2f}\n"
        else:
            print("Valor incorreto")


    elif opcao == 2:
        saque = float(input("Qual valor do saque: "))
             
        if saque < saldo:
            saldo -= saque
            print("Saque realizado")
            numero_saques += 1
            print(numero_saques)
        elif saque> saldo:
            print("Valor maior que seu saldo")


    elif opcao == 3:
        print("Extrato")

    elif opcao == 0:
        break
    
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")