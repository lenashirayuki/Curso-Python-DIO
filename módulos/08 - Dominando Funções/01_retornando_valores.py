def calcular_numeros(numeros):
    return sum(numeros)

def retornar_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def teste_1():
    print("Olá, mundo!") # Se o valor de retorno não for especificado, ele retornará "None".



print(calcular_numeros([1, 2, 3])) # 6
print(retornar_antecessor_e_sucessor(10)) # (9, 11)
print(teste_1()) # None