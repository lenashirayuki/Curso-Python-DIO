# CONHECIMENTOS GERAis DE "IF", "ELSE" E "ELIF".

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe a sua idade: "))

if idade >= MAIOR_IDADE:
    print("Autorizado a tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Autorizado a apenas realizar as aulas teóricas.")
else:
    print("Não autorizado a tirar a CNH.")