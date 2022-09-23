if __name__ == "__main__":  
    main = int(input("Que ejercicio deseas realizar(1,2,3 o 4):"))
    if main == 1:
        from Clases.ejercicio1 import *
        print(matriz)
    if main == 2:
        from Clases.ejercicio2 import *
        palabra = input("Introduce el texto que quieras: ")
        dos = contar(palabra)
        dos
    if main == 3:
        from Clases.ejercicio3 import *
