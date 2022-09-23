from tabulate import tabulate

f =int(input("introduce el numero de filas: "))
c =int(input("introduce el numero de columnas: "))
d=[]
def tabla(f,c,d):
    d = []
    if f<1 or f>9 and c<1 or c>9 :
        print("Error, index out of range...")
    
    elif c<1 or c>9 or f<1 or f>9:
        print("Error, index out of range...")
    else:
        d.append(f)
        d.append(c)
        print(d)
        

tabla(f,c,d)