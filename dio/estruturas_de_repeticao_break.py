while True:
    numero = int(input("Insira um número: "))

    if numero == 10:
        break

    print(numero)

for numero in range(100):
    
    if numero % 2 == 1:
        continue

    print(numero, end=" ")