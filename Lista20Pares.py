pares = range(20)
aux = 0
par = 0

while aux < 20:
    if(par%2==0):
        pares[aux] = par
        aux+=1
    par+=1
    
sum=0
for i in pares:
    sum+=i
    print(i)
    
print("La suma de los números pares es: "+str(sum))
