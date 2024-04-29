conta_normal = 1
contra_universitaria = 2

saldo = 2000
cheque_especial = 250

tipo_de_conta = int(input("Insira o número do seu tipo de conta: \n[1] Normal\n[2] Universitária\n R: "))

if tipo_de_conta == 1:
    print("Conta normal selecionada.")
    print("Saldo atual:", saldo)
    saque = int(input("Defina o valor do saque: "))
    if saque <= saldo:
        print("Realizando saque... Saque realizado com sucesso.")
    elif saque <= (saldo + cheque_especial):
        print("Realizando saque... Saque realizado com cheque especial.")
    else:
        print("Saldo insuficiente para realizar saque.")

elif tipo_de_conta == 2:
    print("Conta especial selecionada.")
    print("Saldo atual:", saldo)
    saque = int(input("Defina o valor do saque: "))
    if saque <= saldo:
        print("Realizando saque... Saque realizado com sucesso.")
    elif saldo < saque:
        print("Saldo insuficiente para realizar o saque.")

print("Obrigado por ser nosso cliente. Tenha um bom dia.")