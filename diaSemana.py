array = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print("Del número del 1 al 7, este programa devuelve el día de la semana "
      "respectivo")
dia=int(input("Ingrese un número del 1 al 7: "))

while dia<1 or dia>7:
    dia = int(input("Ingrese un número del 1 al 7: "))
    
print("El día de la semana es "+array[dia-1])
