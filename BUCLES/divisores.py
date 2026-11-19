numero = int(input("Introduce un número: "))
x=int((numero/2)+1)
for i in range(1, x):
    if numero % i == 0:
        print(i)
print(numero)