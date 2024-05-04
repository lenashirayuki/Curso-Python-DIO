# IF ANINHADO: São estruturas dentro de outra estruturas. Exemplo, um "If" pode existir dentro de um outro "If".

conta_normal = 1
contra_universitaria = 2

saldo = 2000
cheque_especial = 250

tipo_de_conta = int(input("Insira o número do seu tipo de conta: \n[1] Normal\n[2] Universitária\n R: "))

if tipo_de_conta == 1:
    print("Conta normal selecionada.")
    opcao = int(input("Escolha uma das opções: \n[1] Sacar\n[2] Voltar\n R: "))
    if opcao == 1:
        print("Saldo atual:", saldo)
        saque_1 = int(input("Defina o valor que deseja sacar: ")):
        if saldo > saque_1:
            print("Realizando saque... saque realizado com sucesso.")
        elif saque_1 <= (saldo + cheque_especial):
            print("Realizando saque... saque realizado com cheque especial.")
        else:
            retorno = int(input("Saldo insuficiente para realizar o saque. Deseja voltar para tela inicial?\n[1] Sim\n[2] Não")):
            if retorno == 1: return opcao


elif tipo_de_conta == 2:
    print("Conta especial selecionada.")
    print("Saldo atual:", saldo)
 opcao = int(input("Defina o valor do opcao: "))
    if opcao <= saldo:
        print("Realizando opcao... opcao realizado com sucesso.")
    elif saldo < opcao:
        print("Saldo insuficiente para realizar o opcao.")

print("Obrigado por ser nosso cliente. Tenha um bom dia.")