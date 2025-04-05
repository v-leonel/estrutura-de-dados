# 4. Inverter um array
# Crie um programa que inverta os elementos de um array sem usar a função reverse().

# Entrada: [1, 2, 3, 4, 5]
# Saída esperada: [5, 4, 3, 2, 1]

# 💡 Dica: Você pode usar slicing [::-1] ou um loop for

array = [1, 2, 3, 4, 5]
def InverterArray(array):
    arrayInvertido = []
    
    for i in array[::-1]:
        arrayInvertido += [i]
        
    return print(arrayInvertido)
        
InverterArray(array)