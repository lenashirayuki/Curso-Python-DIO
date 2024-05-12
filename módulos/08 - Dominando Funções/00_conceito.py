# Função é um bloco de códigos. Ele recebe um nome e esse nome é o que identifica o agrupamento;
# É possível enviar parâmetros para a função;
# Ela pode retornar valores. Não somente um, mas vários;
# Programar baseado em funções é o mesmo que dizer que estamos programando de maneira estruturada.


# Exemplos de funções básicas:

def exibir_mensagem():
    print("Olá, mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem-vindo(a), {nome}!")

def exibir_mensagem_3(nome= "Anônimo"):
    print(f"Seja bem-vindo(a), {nome}!")

# Chamando as funções:

exibir_mensagem()
exibir_mensagem_2(nome="Helena")
exibir_mensagem_3()
exibir_mensagem_3(nome="Marina")