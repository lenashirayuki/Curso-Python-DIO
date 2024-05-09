# Para acessar valores, utiliza-se os colchetes quase que da mesma maneira que fizemos para atribuir um valor.

pessoa = {"nome": "Helena", "idade": "19 anos"}
pessoa["telefone"] = "1234-5678"

# Peguemos o último exemplo. Ao invés de colocarmos o valor de igualdade para atribuir o valor, pegamos a primeira parte e usamos "print".
# O código entenderá que não é uma atribuição, e sim um pedido para revelar qual o valor daquela chave.

print(pessoa["telefone"]) # "1234-5678"
print(pessoa["nome"]) # "Helena"
print(pessoa["idade"]) # "19 anos"

# Mas caso alguém deseje fazer uma atribuição, o código irá permitir.

pessoa["nome"] = "Marina"
pessoa["telefone"] = "0987-6543"
pessoa["idade"] = "20 anos"

print(pessoa) # "{'nome': 'Marina', 'idade': '20 anos', 'telefone': '0987-6543'}" — Valores alterados com sucesso.