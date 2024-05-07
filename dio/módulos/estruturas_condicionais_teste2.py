# TESTES DE COMANDOS 2

opcao = int(input("Escolha uma das opções: \n[1] Sacar \n[2] Ver extrato\n R:"))

if opcao == 1:
    valor = float(input("Defina o valor de saque: "))
elif opcao == 2:
    print("Exibindo extrato...")
else:
    SystemExit("Opção inválida.")