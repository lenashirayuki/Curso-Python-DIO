# Também é possível utilizar o índice nos conjuntos.

carros = {"Gol", "Celta", "Pálio", "Celta"}

for indice, veiculos in enumerate(carros):
    print(f"{indice}: {veiculos}")

# ========= Resultado:
# 0: Celta
# 1: Gol
# 2: Pálio