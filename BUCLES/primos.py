#Toma un número y comprueba si es primo o no

n= int (input("Introduce un número: "))

if n <= 1:
        print("El", n, "no es primo")

for i in range(2, int(n/2)+1):
        if n % i == 0:
                print ("El", n, " no es primo")
                break
else:
       print("El", n, " es primo")