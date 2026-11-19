#Modifica el ejercicio anterior de manera que te pida números, 
#te diga si es primo y termine cuando le des un cero
while True:
    n= int (input("Introduce un número: "))

    if n == 0:
        print("Fin programa")
        break

    if n <= 1:
        print("El", n, "no es primo")

    for i in range(2, int(n/2)+1):
        if n % i == 0:
            print ("El", n, " no es primo")
            break
    else:
        print("El", n, " es primo")