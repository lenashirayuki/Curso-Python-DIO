# A principal diferença dos métodos dos conjuntos é que é possível realizar operações matemáticas únicas.



# {}.union = união: une ambos os conjuntos.

conjunto_a = {1, 2, 3}
conjunto_b = {1, 3, 5, 6, 7}
print(conjunto_a.union(conjunto_b)) # {1, 2, 3, 5, 6, 7}

# {}.intersection = intersecção: apenas os valores iguais nos dois conjuntos.

conjunto_a = {1, 2, 3}
conjunto_b = {1, 3, 5}
print(conjunto_a.intersection(conjunto_b)) # {1, 3}

# {}.difference = diferença: aquilo que está em um conjunto e que não está no outro.

conjunto_a = {1, 2, 3}
conjunto_b = {1, 3, 5}
print(conjunto_a.difference(conjunto_b)) # {2}
print(conjunto_b.difference(conjunto_a)) # {5}

# {}.symmetric_difference = diferença simétrica: aqueles valores que não fazem parte da intersecção em ambos os conjuntos.

conjunto_a = {1, 2, 3}
conjunto_b = {1, 3, 5}
print(conjunto_a.symmetric_difference(conjunto_b)) # {2, 5}

# {}.issubset: se todos os valores de um conjunto pertencem a outro (o resultado volta em "True" ou "False").

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5, 6}
print(conjunto_a.issubset(conjunto_b)) # "True" pois tudo do conjunto A está no conjunto B;
print(conjunto_b.issubset(conjunto_a)) # "False" pois nem tudo do conjunto B está no conjunto A.

# {}.issuperset: é o contrário do "issubset"; se todos os valores de um conjunto contemplam os valores do outro.

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5, 6}
print(conjunto_a.issuperset(conjunto_b)) # "False" pois A não contempla tudo que está em A;
print(conjunto_b.issuperset(conjunto_a)) # "True" pois B contempla tudo que está em B.

# {}.isdisjoint: conjuntos que não se tocam; o resultado será verdadeiro se os conjuntos selecionados não tiverem valores em comum.

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5, 6}
conjunto_c = {4, 5, 6}
print(conjunto_a.isdisjoint(conjunto_c)) # "True" porque nenhum dus valores dos conjuntos A e C se intersectam;
print(conjunto_b.isdisjoint(conjunto_c)) # "False" pois há valores em B que pertecem a C.

# {}.add = adicionar: adiciona um valor àquele conjunto (dahnn). Elementos já existentes não serão adicionados.

sorteio = {1, 2, 3, 25, 36}
sorteio.add(40)
sorteio.add(50)
sorteio.add(40)
print(sorteio) # {1, 2, 3, 36, 50, 40, 25} — Os valores no comando de "add" foram adicionados no final.

# {}.clear = limpar: limpa o conjunto.

sorteio = {1, 2, 3, 25, 36}
sorteio.clear()
print(sorteio) # {}

# {}.copy = copiar: vai copiar o conjunto.

sorteio = {1, 2, 3, 25, 36}
print(sorteio)
print(sorteio.copy()) # Apesar de serem os mesmo valores do conjunto, possuem IDs diferentes.

# {}.discard: descarta o valor selecionado do conjunto.

sorteio = {1, 2, 3, 25, 36, 50, 100, 120, 300}
sorteio.discard(2)
sorteio.discard(100)
sorteio.discard(300)
print(sorteio) # {1, 3, 36, 50, 120, 25} — Como feito no código, os valores mencionados foram descartados.

# {}.pop: tira os valores da lista um por um. Ao invés de começar pelo último valor, ele começa pelo primeiro.

sorteio = {1, 2, 3, 25, 36, 50, 100, 120, 300}
sorteio.pop()
sorteio.pop()
sorteio.pop()
sorteio.pop()
print(sorteio) # {36, 300, 50, 120, 25} — Tirou os quatro primeiros valores.

# {}.remove: bem parecido com o "discard", mas diferente dele, apresentará erro caso peça para remover um valor não-existente.

sorteio = {1, 2, 3, 25, 36, 50, 100, 120, 300}
sorteio.remove(1) # Esse valor existe no conjunto acima, então será removido;
sorteio.remove(45) # Esse valor não existe, logo ocorrerá um erro.

# len: mede o tamanho daquele conjunto.

numeros = {1, 2, 3, 3, 3, 3, 3, 25, 36, 50, 100, 120, 300}
print(len(numeros)) # Ele retornou "9" como valor. O código desconsiderou os números repetidos no conjunto.

# In: pode ser usado para verificar se um elemento está dentro daquele conjunto.

numeros = {1, 2, 3, 3, 3, 3, 3, 25, 36, 50, 100, 120, 300}
print(1 in numeros) # "True" pois o número citado faz parte do conjunto;
print(1000 not in numeros) # "True" também porque o número citado não faz parte do conjunto (not in);
print(1000 in numeros) # "False" pois o número não está no conjunto (in).