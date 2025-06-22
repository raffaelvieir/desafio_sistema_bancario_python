menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao  = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito = float(input("insira o valor que dejesa depositar R$: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("Valor informado inválido, tente novamente!")
    elif opcao == "s":
        saque = float(input("Informe o valor que deseja sacar R$: "))
        saldo_excedido = saque > saldo
        limite_excedido = saque >limite 
        saque_excedido = numero_saques >= LIMITE_SAQUES
        if saldo_excedido:
            print("Saldo insuficiente!")
        elif limite_excedido:
            print(" O valor do saque excede o limite!")
        elif saque_excedido:
            print("Número máximo de saques permitido foi excedido!")
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques =+1
        else:
            print("O valor informado é inválido")

    elif opcao == "e":
        print("\n======Extrato======\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nsaldo: R${saldo:.2f}")
        print("====================")
    
    elif opcao == "q":
        print("Saíndo")
        break
    else:
        print("Opereção Inválida, por favor selecione a operação desejada!")
