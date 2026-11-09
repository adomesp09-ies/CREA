cpar = 0
cimpar = 0

for i in range(1, 11):
    n=int(input("Introduce un número: "))
    if n%2==0:
        cpar = cpar + 1
    else:
        cimpar = cimpar + 1
    
print("hay", cpar, "números pares")
print("hay", cimpar, "números impares")