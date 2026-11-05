A=int(input("Introduce un número: "))
B=int(input("Introduce otro número: "))
C=int(input("Introduce otro número: "))

if A>B and A>C and B>C:
  print(C, B, A)

if A>B and A>C and B<C:
    print(B, C, A)

if A<B and A<C and B>C:
    print(A, C, B)

if A<B and A<C and C>B:
    print(A, B, C)

if C>B and C>A and B<A:
    print(B, A, C)

if B>A and B>C and A>C:
    print(C, A, B)