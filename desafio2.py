



def menu():
    return input("""
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de R${valor:.2f} concluído\n"
    else:
        print("Valor inválido para depósito")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def extrato(saldo, /, *, extrato):
    return 0

def main():
    saldo = 0
    limite = 500
    extrato = ""
    LIMITE_SAQUES = 3
    numero_saques = 0
    while True:
        opcao = str(menu())

        if opcao == "d":
            valor = float(input("Quanto deseja depositar?\n"))
            saldo, extrato = depositar(saldo, valor, extrato, )

        elif opcao == "s":
            if LIMITE_SAQUES > 0:
                if saldo > 0:
                    valor = float(input("Quanto deseja sacar?\n"))
                    saldo, extrato = sacar(saldo = saldo,valor = valor,extrato = extrato,limite = limite,numero_saques = numero_saques,limite_saques = LIMITE_SAQUES)
                else:
                    print("Saldo insuficiente para saque")
            else:
                print("Limite de saques diários excedido, não é póssivel sacar mais por hoje \n")

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            print(f"{extrato}\n" if extrato else "Não houve movimentações na conta")
            print(f"R${saldo:.2f}")
            print("==========================================")

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
