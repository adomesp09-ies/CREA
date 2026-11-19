#Toma un número y comprueba si es primo o no

n= int (input("Introduce un número: "))
div=0

for i in range(1, n + 1):
    if n % i == 0:
            div=div+1
            
if div==0 or n==1:
    print("El", n, "es primo")
else:
    print("El", n, " no es primo")
