# evTema1

El link de este repositorio es [GitHub](https://github.com/joseluis031/evTema1.git)

![Captura](https://user-images.githubusercontent.com/91721888/192027003-9cb0940a-ef6b-484d-9d19-7e878150f21b.jpg)

## Main
```
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
    if main == 3:  #he intentado varias formas pero no he conseguido que me de todas las listas, por separado si
        from Clases.ejercicio3 import *
    if main ==4:
        from Clases.ejercicio4 import *
        filas =int(input("introduce el numero de filas: "))
        column =int(input("introduce el numero de columnas: "))
        cuatro = tabla(filas,column)
´´´
        

