# ============== PARÂMETROS SOMENTE POR POSIÇÃO:


def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    # A parte antes da barra, na chamada da função, tem que vir na ordem correta;
    # Já a segunda parte, não precisa, pois podemos direcionar valores para cada um desses parâmetros.
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", combustivel="Gasolina", motor="1.0")
 # Essa é uma instrução válida, pois segue todas as regras;

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", combustivel="Gasolina", motor="1.0")
# Já essa, é inválida, pois os três primeiros parâmetros não podem receber chaves.


# ============== PARÂMETROS SOMENTE POR NOME:


def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    # Todos agora devem receber uma chave.
    print(modelo, ano, placa, marca, combustivel, motor)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", combustivel="Gasolina", motor="1.0")


# ============== PARÂMETROS HÍBRIDO:


def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    # A primeira parte é por posição (obrigátorio); a segunda, pode ser tanto por posição, quanto por nome.
    print(modelo, ano, placa, marca, combustivel, motor)

criar_carro("Palio", 1999, "ABC-1234", "Fiat", combustivel="Gasolina", motor="1.0")
