# 2. Encontrar o maior e o menor valor
# Dado um array de números, encontre e imprima o maior e o menor valor presente nele.

# Entrada: [5, 8, 2, 10, 3]
# Saída esperada: [2, 10]


def MaiorEMenorValor(array=[5, 8, 2, 10, 3]):
    maiorValor = array[0]           #inicializa no indice zero do array
    menorValor = array[0]           #inicializa no indice zero do array

    for indice in array:            #para cada indice no array
        if indice < menorValor:     #verificar se o indice tem valor menor que o indice zero
            menorValor = indice     #se verdadeiro troca o menorValor pelo valor do indice
        elif indice > maiorValor:   #verificar se o indice tem valor maior que o indice zero
            maiorValor = indice     #se verdadeiro troca o maiorValor pelo valor do indice
            
    encontrado = [menorValor,maiorValor]
            
    return print(encontrado)

MaiorEMenorValor()

                
    
    