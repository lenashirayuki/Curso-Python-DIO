def somar(a, b):
    return a + b

def mostrar_resultado(a, b, funcao):
    resultado =  funcao(a, b)
    print(f"O resultado da função {a} + {b} = {resultado}")

mostrar_resultado(10, 10, somar)  # O resultado da função 10 + 10 = 20