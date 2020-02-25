primeraC = raw_input("Ingrese la primera cadena de texto: ")
segundaC = raw_input("Ingrese la segunda cadena de texto: ")

if len(primeraC) != len(segundaC):
    print("Las cadenas de texto no son iguales")
else: 
    for i in range(len(primeraC)):
        if primeraC[i] != segundaC[i]:
            print("Las cadenas de texto no son iguales")
            break
    print("Las cadenas de texto son iguales")
