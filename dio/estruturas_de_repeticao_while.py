opcao = -1

while opcao != 0:
    opcao = int(input("Escolha uma opção:\n[1] Sacar.\n[2] Ver saldo.\n[0] Fechar sistema.\n R: 3"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Mostrando saldo...")
else:
        print("Obrigado por usar o nosso sistema.")