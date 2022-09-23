matriz = [

    [1, 1, 1, 3],

    [2, 2, 2, 7],

    [3, 3, 3, 9],

    [4, 4, 4, 13]

]


def matriz2(matriz):
    for i in range(len(matriz)):
        suma = matriz[slice(len(matriz)-1)]
        matriz[i][3] = sum(suma) #selecciono la columna que quiero de cada fila


uno = matriz2(matriz)
print(uno)