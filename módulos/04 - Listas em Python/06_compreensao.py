# Primeira versão (mais complicada):

numeros = [1, 10, 23, 21, 15, 30, 100, 50, 65]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

# Segunda versão (mais simples):

numeros = [1, 10, 23, 21, 15, 30, 100, 50, 65]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificando na versão 1:

numeros = [1, 10, 23, 21, 15, 30, 100, 50, 65]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
print(quadrado)

# Modificando na versão 2:

numeros = [1, 10, 23, 21, 15, 30, 100, 50, 65]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)