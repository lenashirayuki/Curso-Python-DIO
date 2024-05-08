nome = "Helena"
idade = 19
profissão = "Estudante"
linguagem = "Python"
saldo = 245.890

dados = {"nome": "Helena", "idade": 19}


print("Nome: %s Idade: %d Profissão: %s Linguagem: %s" % (nome, idade, profissão, linguagem))

print("Nome: {} Idade: {} Profissão: {} Linguagem: {}".format(nome, idade, profissão, linguagem))
print("Nome: {1}, Idade: {0}, Profissão: {3}, Linguagem: {2}.".format(idade, nome, linguagem, profissão))
print("Nome: {nome}, Idade: {idade}.".format(nome=nome, idade=idade))
print("Nome: {nome}, Idade: {idade}.".format(**dados))

print(f"Nome: {nome}, Idade: {idade}, Saldo: {saldo:.0f}.")