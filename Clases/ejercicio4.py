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
        for i in range(len(d)):
            d.append(f)
            print(d)
        

tabla(f,c,d)