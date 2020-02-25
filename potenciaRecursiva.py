def potencia(num,exp):
    if exp == 0:
        return 1
    elif num < 0:
        return potencia(num, exp+1)/num
    elif exp > 0:
        return num*potencia(num, exp-1)
    
num = int(input("Ingrese el número: "))
exp = int(input("Ingrese el exponente: "))

print("El resultado de la operación es: "+str(potencia(num,exp)))
