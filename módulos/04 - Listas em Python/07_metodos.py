# MÉTODO ============================= [].Append


lista = []

lista.append(1)
lista.append("Helena")
lista.append("Yasmin")
lista.append(2 ** 2)
lista.append([40, 30, 20, 100, 200])

print(lista)


# MÉTODO ============================= [].Clear


lista = [40, 30, 20, 100, 200]
lista.clear()

print(lista)


# MÉTODO ============================= [].Copy


lista = [40, 30, 20, 100, 200]
l2 = lista.copy()

print(lista)

print(id(l2), id(lista))

l2[0] = 2

print(l2)
print(lista)


# MÉTODO ============================= [].Count


frutas = ["maçã", "maçã", "pera", "uva", "mamão", "mamão", "mamão"]

f1 = frutas.count("maçã")
f2 = frutas.count("mamão")
f3 = frutas.count("uva")

print(f1)
print(f2)
print(f3)


# MÉTODO ============================= [].Extend


linguagens = ["Java", "JavaScript", "C++"]
linguagens.extend(["Python", "LUA"])

print(linguagens)


# MÉTODO ============================= [].Index


pessoas = ["Marina", "Helena", "Felicia", "Ophelia"]
print(pessoas.index("Marina"))
print(pessoas.index("Helena"))
print(pessoas.index("Felicia"))
print(pessoas.index("Ophelia"))


# MÉTODO ============================= [].Pop


pilha = ["verde", "vermelho", "azul", "amarelo"]
print(pilha.pop())
print(pilha.pop())
print(pilha.pop())
print(pilha.pop(0))


# MÉTODO ============================= [].Remove


linguagens = ["Java", "JavaScript", "C++", "Python", "CSharp", "Java"]

for java in linguagens:
    if "Java" in linguagens:
        linguagens.remove("Java")
print(linguagens)


# MÉTODO ============================= [].Reverse


linguagens = ["Java", "JavaScript", "C++", "Python", "CSharp", "Java"]
linguagens.reverse()

print(linguagens)


# MÉTODO ============================= [].Sort


linguagens = ["Java", "JavaScript", "C++", "Python", "CSharp"]
linguagens.sort()
print(linguagens)

linguagens = ["Java", "JavaScript", "C++", "Python", "CSharp"]
linguagens.sort(reverse=True)
print(linguagens)

linguagens = ["Java", "JavaScript", "C++", "Python", "CSharp"]
linguagens.sort(key=lambda x: len(x))
print(linguagens)

linguagens = ["Java", "JavaScript", "C++", "Python", "CSharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)


# MÉTODO ============================= Len


linguagens = ["Java", "JavaScript", "C++", "Python", "CSharp"]
print(len(linguagens))