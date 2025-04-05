# 5. Remover duplicatas de um array
# Dado um array com números repetidos, remova as duplicatas e imprima a lista sem repetições.

# Entrada: [1, 2, 2, 3, 4, 4, 5]
# Saída esperada: [1, 2, 3, 4, 5]

# 💡 Dica: Converta a lista para um set e depois para list.

array = [0,0,1,1,1,2,2,3,3,4]

def RemoveDuplicatas(array):
    arraySemDuplicatas = []
    
    for i in array:
        if i not in arraySemDuplicatas:
            arraySemDuplicatas += [i]
            
    print(arraySemDuplicatas)
    
RemoveDuplicatas(array)