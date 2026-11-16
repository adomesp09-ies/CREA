N1 = int(input("Introduce un número: "))
N2 = int(input("Introduce otro número: "))

if N1 % N2 == 0:
    print(N1, "es divisor de", N2)
else:
    print(N1, "no es divisor de", N2)