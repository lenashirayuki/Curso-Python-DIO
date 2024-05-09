# Também é possível iterar dicionários.

contatos = {
    "helena@gmail.com": {"nome": "Helena", "idade": "19 anos", "telefone": "1234-5678"},
    "marina@gmail.com": {"nome": "Marina", "idade": "20 anos", "telefone": "8765-4321"},
    "felicia@gmail.com": {"nome": "Felicia", "idade": "22 anos", "telefone": "0987-6543"}
}

# Primeira forma de iterar (menos utilizada):

for chave in contatos:
    print(chave, contatos[chave])

# Segunda forma de iterar (utilizando o método "items", que será explicado mais pra frente):

for chave, valor in contatos.items():
    print(chave, valor)