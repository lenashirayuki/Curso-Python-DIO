menu = """

    [0] Depositar
    [1] Sacar
    [2] Exibir extrato
    [3] Sair

==> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "0":
        
        valor = float(input("Insira o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"- Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso.")

        else:
            print("Operação falhou. O valor informado é inválido.")
    
    elif opcao == "1":
        
        saque = float(input("Insira o valor que deseja sacar: "))

        excedeu_saldo = saque > saldo

        excedeu_limite = saque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente para realizar a transação. Tente novamente.")
        
        elif excedeu_limite:
            print("Limite de saldo para saque ultrapassado. Tente novamente.")
        
        elif excedeu_saques:
            print("Numero de saques máximos realizados. Tente em outro momento.")
        
        elif saque < saldo:
            saldo -= saque
            numero_saques += 1
            extrato += f"- Saque: R$ {saque:.2f}\n"
            print("Saque realizado com sucesso.")
        
        else:
            print("Valor inválido. Tente novamente.")


    elif opcao == "2":
        print("<=========== EXTRATO ===========>")
        print("Não foram realizadas movimentações.") if not extrato else extrato
        print(extrato)
        print(f"""
              
Saldo total na conta: {saldo:.2f}""")
        print("<===============================>")
    
    elif opcao == "3":
        break

    else:
        print("Opção inválida. Selecione outro número.")