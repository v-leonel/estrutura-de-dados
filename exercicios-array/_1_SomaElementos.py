#1. Soma dos elementos do array
# Crie um programa que percorra um array de números inteiros e calcule a soma de todos os elementos.

# Entrada: [10, 20, 30, 40, 1]
# Saída esperada: 101

# 💡 Dica: Use um loop for ou a função sum().

array = [10, 20, 30, 40, 1]

def SomaElementosComFor(array):
    soma = 0
    for indice in array:
        soma += indice 
    return print(soma)

def SomaElementosComSum(array):
    return print(sum(array))

SomaElementosComFor(array)
SomaElementosComSum(array)

