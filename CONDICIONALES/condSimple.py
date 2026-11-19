n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))
n3 = int(input("Introduce el tercer número: "))

if n1 <= n2:
    if n2 <= n3:
        print(n1, n2, n3)
    else:
        if n1 <= n3:
            print(n1, n3, n2)
        else:
            print(n3, n1, n2)
else:
    if n1 <= n3:
        print(n2, n1, n3)
    else:
        if n2 <= n3:
            print(n2, n3, n1)
        else:
            print(n3, n2, n1)
