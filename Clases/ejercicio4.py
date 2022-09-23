
def tabla(filas,column):
    
    
    if filas<1 or filas>9 and column<1 or column>9 :
        print("Error, index out of range...")
    
    elif column<1 or column>9 or filas<1 or filas>9:
        print("Error, index out of range...")
    else:
        for f in range(filas):
            print(" ")
            for c in range(column):
                print(" * ", end='')
        

