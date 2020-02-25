def suma(x):
    if x == 0:
        return 0
    else:
        return x + suma(x-1)
resul = int(input("Ingrese el n: "))
print(suma(resul))
