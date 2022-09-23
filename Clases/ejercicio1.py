matriz = [

    [1, 1, 1, 3],

    [2, 2, 2, 7],

    [3, 3, 3, 9],

    [4, 4, 4, 13]

]


for i in range(len(matriz)):
    filas = matriz[i]
    suma = filas[slice(len(matriz)-1)]
    matriz[i][3] = sum(suma) #selecciono la columna que quiero de cada fila

