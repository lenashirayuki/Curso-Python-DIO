# A principal maneira de declarar um dicionário é por meio das chaves /{}/, mas não a única.
# Dentro delas, armazenamos a "chave" para um determinado valor. Esses valores não se repetem (igual nos conjuntos) e são mutáveis.
# A única coisa que é imutável e não pode ser alterada é a chave respectiva daquele valor.

# 1ª forma de declarar (utilizando o sinal das chaves):

pessoa = {"nome": "Helena", "idade": 19} # Aqui colocamos "nome" como a chave para o valor "Helena".

# 2ª forma de declarar (utilizando "dict"):

pessoa = dict(nome="Helena", idade=19) # Como chamamos a classe "dict", não precisamos utilizar o sinal de chaves.

# 3ª forma de declarar (utilizando o sinal de colchetes):

pessoa["telefone"] = "1234-5678"

# Resultado final com todos os valores declarados até o momento:

print(pessoa) # {'nome': 'Helena', 'idade': 19, 'telefone': '1234-5678'}