# Assim como outras classes, aqui também possui métodos. Muitos serão repetidos de outras classes.



# {}.clear: limpa o dicionário.


contatos = {
    "helena@gmail.com": {"nome": "Helena", "idade": "19 anos", "telefone": "1234-5678"},
    "marina@gmail.com": {"nome": "Marina", "idade": "20 anos", "telefone": "8765-4321"},
    "felicia@gmail.com": {"nome": "Felicia", "idade": "22 anos", "telefone": "0987-6543"}
}

contatos.clear()
print(contatos) # {}


# {}.copy: tira uma cópia do dicionário.


contatos = {
    "helena@gmail.com": {"nome": "Helena", "idade": "19 anos", "telefone": "1234-5678"},
}

copia = contatos.copy()
copia["helena@gmail.com"] = {"nome": "Ellie"} # Atribuímos novos valores à cópia. A atribuição deve ser feita com chaves.

print(contatos) # {'helena@gmail.com': {'nome': 'Helena', 'idade': '19 anos', 'telefone': '1234-5678'}}
print(copia) # {'helena@gmail.com': {'nome': 'Ellie'}}


# {}.fromkeys: comando que irá criar chaves para você. Elas podem ficar sem nenhum valor atribuído ou até receberem dentro do próprio código.


print(dict.fromkeys(["nome", "idade"])) # {'nome': None, 'idade': None}
print(dict.fromkeys(["nome", "idade"], "vazio")) # {'nome': 'vazio', 'idade': 'vazio'}


# {}.get: outro meio de acessar valores dentro de um dicionário


contatos = {
    "helena@gmail.com": {"nome": "Helena", "idade": "19 anos", "telefone": "1234-5678"},
}

# contatos["chave"] # Nesse caso, como não existe uma chave chamada "chave", o programa irá parar;

contatos.get("chave") # Ele irá retornar "None" pois não existe valor atribuído a essa chave;
contatos.get("chave", {}) # Ocorrerá a mesma coisa do exemplo anterior, mas ao invés disso, ele me retornará o sinal depois da vírgula se não tiver nada atribuido.
contatos.get("helena@gmail.com", {}) # {"helena@gmail.com": {"nome": "Helena", "idade": "19 anos", "telefone": "1234-5678"}}


# {}.items: retorna apenas a lista de tuplas.


contatos = {
    "helena@gmail.com": {"nome": "Helena", "idade": "19 anos", "telefone": "1234-5678"},
}


print(contatos.items()) # dict_items([('helena@gmail.com', {'nome': 'Helena', 'idade': '19 anos', 'telefone': '1234-5678'})])


# {}.keys: retorna apenas as chaves.


contatos = {
    "helena@gmail.com": {"nome": "Helena", "idade": "19 anos", "telefone": "1234-5678"},
}

print(contatos.keys()) # dict_keys(['helena@gmail.com'])


# {}.pop: ele remove a chave e o seu valor correspondente