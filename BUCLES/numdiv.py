#Toma un número de entrada y visualiza el número de divisores 
# que tiene. Ej si le das el 12 debe devolver: 
# el 12 tiene 6 divisores

n = int(input("Introduce un número: "))
div = 0

for i in range(1, n + 1):
    if n % i == 0:
        div += 1

print("El", n, "tiene", div, "divisores")