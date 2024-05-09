# Dicionarios aninhados são estruturas dentro da outra. Assim como nas tuplas, listas e conjuntos, fazer isso aqui também é possível.
# No caso de dicionários, fazer matrizes igual nos outros tipos de "listas" não se prova útil; mas, em contra partida, podemos armazenar...
# dados que possam vir a ser úteis. No exemplo abaixo isso fica melhor exemplificado.

contatos = {
    "helena@gmail.com": {"nome": "Helena", "idade": "19 anos", "telefone": "1234-5678"},
    "marina@gmail.com": {"nome": "Marina", "idade": "20 anos", "telefone": "8765-4321"},
    "felicia@gmail.com": {"nome": "Felicia", "idade": "22 anos", "telefone": "0987-6543"}
}

# Pela criação desse dicionário com todas essas informações, podemos acessar o contato de alguns desses emails fictícios:

exemplo_1 = contatos["helena@gmail.com"]["telefone"]
print(exemplo_1) # Retornou a informação desejada: "1234-5678"

