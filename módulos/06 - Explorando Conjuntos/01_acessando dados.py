# Dados de um "set" não podem ser acessados até que sejam convertidos.

# ============ Exemplo 1 (não funcionou):


carros_1 = set(("Gol", "Celta", "Pálio", "Pálio", "Celta"))
print(carros_1[0]) # "TypeError: 'set' object is not subscriptable."


# ============ Exemplo 2 (funcionou):


carros_2 = set(("Gol", "Celta", "Pálio", "Pálio", "Celta"))
carros_2 = list(carros_2) # Método de converter
print(carros_2[0]) # Dessa maneira, ele revela que o objeto "0" é "Gol."