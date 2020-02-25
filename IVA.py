def iva(valor):
    iva = valor*0.16
    return iva
valor = int(input("Ingrese el valor del producto"))
print("El valor del IVA es: " + str(float(iva(valor))) +
      "\n El precio total del producto es: " + str(float(valor+iva(valor))))
