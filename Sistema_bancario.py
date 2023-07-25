menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite_saque = 500
numero_saque = 3
extrato = ""
qtd_saque = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"

        else:
            print("Erro de operação, valor informado é inválido")



    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_saque

        excedeu_saque = qtd_saque >= numero_saque

        if excedeu_saldo:
            print("Saldo insuficiente.")

        elif excedeu_limite:
            print("Valor excede o limite de saque, por favor insira um valor de até R$ 500,00.")

        elif excedeu_saque:
            print("Limite de 3 saques excedido, por favor volte amanhã.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            qtd_saque += 1

        else:
            print("Operação inválida, por favor tente novamente.")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================")

    elif opcao == "q":
        print("Obrigado por utilizar nossos serviços, volte sempre!")
        break

    else:
        print("Operação inválida, selecione alguma das opções")