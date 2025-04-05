# 3. Contar elementos pares e ímpares
# Dado um array de números inteiros, conte quantos são pares e quantos são ímpares.

# Entrada: [1, 2, 3, 4, 5, 6]
# Saída esperada:

# Pares: 3  
# Ímpares: 3  
# 💡 Dica: Use o operador % para verificar se um número é par (num % 2 == 0).


array = [1, 2, 3, 4, 5, 6]

def ContarElementosParesEImpares(array):
    pares = 0
    impares = 0
    for i in array:
        if i % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1
    
    return print([pares,impares])

ContarElementosParesEImpares(array)