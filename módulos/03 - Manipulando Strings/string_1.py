nome = "hElEnA"

print(nome.upper())
print(nome.lower())
print(nome.title())


texto = " Olá, mundo!    "

print(texto.lstrip())
print(texto.rstrip())
print(texto.strip())


menu = "Python"

for letra in menu:
    print(letra, end="-")

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("P-y-t-h-o-n")
print("-".join(menu))