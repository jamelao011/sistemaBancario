menu = """
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).upper()

    if opcao == "D":
        print("Depósito")
        deposito = float(input("Digite o valor do depósito: "))
        if deposito > 0:    
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print("Depósito efetuado com sucesso!!!")
        else:
            print("Valor negativo.")

    if opcao == "S":
        print("Saque")
        if numero_saques < 3:
            saque = float(input("Digite o valor do saque: "))
            if saldo >= saque:
                if saque > 500:
                    print("Limite máximo de saque é de R$ 500 por saque, tente outro valor.")
                else:
                    saldo -= saque
                    numero_saques += 1
                    extrato += f"Saque: R$ {saque:.2f}\n"
                    print(f"Saque efetuado com sucesso!!! Saques restantes: {3 - numero_saques}")
            else:
                print("Saldo insuficiente.")
        else:
            print("Limite máximo diário de saques atingido.")
    
    elif opcao == "E":
        print("\n=============== Extrato ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}")
        print("========================================")

    elif opcao == "Q":
        break
