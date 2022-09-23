print(list(range(11)))
print(list(range(-10,0)))
print(list(range(-20,0,2)))
print(list(range(-19,0,2)))
print(list(range(0,55,5)))



while True:
    x = int(input("inicio?"))
    x2 = int(input("final?"))
    if not x2 == int:
        print(list(range(x)))
        x3 = int(input("separacion?"))
    if not x3 == int:
        print(list(range(x,x2)))
        pass
    x3 = int(input("separacion?"))
    if not x3 == int:
        print(list(range(x,x2)))
    else:
        print(list(range(x,x2,x3)))
    break
