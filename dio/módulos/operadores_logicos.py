# Na condição "AND", todos os valores devem ser verdadeiros para ser "True."
# Na condição "OR", apenas um dos valores deve ser verdadeiro.

print(True and True)
print(True and False)
print(False and False)
print(True or False)
print(True or True)
print (False or False)

saldo = 1500
saque = 400
limite = 200
conta_chefe = True

ex = (saldo >= saque and limite <= saldo) or (conta_chefe and saque <= limite)
print(ex)