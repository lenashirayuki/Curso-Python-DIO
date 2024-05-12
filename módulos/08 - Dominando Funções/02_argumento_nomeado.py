# Funções também podem ser chamadas usando argumentos nomeados com chave=valor.

def salvar_carro(marca, modelo, ano, placa):
    # Salva carro no banco de dados.
    print(f"Carro inserido com sucesso! Marca: {marca}; modelo: {modelo}; ano: {ano}; placa: {placa}.")


salvar_carro("Fiat", "Uno", "2000", "ABC-1234")
 # Valores colocados na sequência da função. A desvantagem é que qualquer troca de valor não impedirá o código de ser executado;

salvar_carro(marca="Fiat", modelo="Uno", ano="2002", placa="DEF-5678")
 # Valores colocados na chamada da função. O código dará erro caso os argumentos sejam alterados na função;

salvar_carro(**{"marca": "Fiat", "modelo": "Uno", "ano": "2002", "placa": "DEF-5678"})
 # Os valores foram colocado em dicionário, ou seja, tanto a chave, quanto o valor do argumento, serão passados.
 
# NOTA: é possível definir os parâmetros obrigatórios com "args" e "kwargs". Quando esses são definidos (*args e **kwargs), o método...
# recebe os valores como TUPLA e DICIONÁRIO respectivamente.