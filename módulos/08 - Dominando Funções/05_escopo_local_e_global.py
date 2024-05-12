salario = 2000 

def bonus_aplicado(bonus):
    global salario # Apesar a variável "salário" ter sido definida na raiz do código, na função, precisamos informar se ela é global.
    salario += bonus
    return salario

print(bonus_aplicado(500))