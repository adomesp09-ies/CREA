A= int(input("Introduce un número: "))
B= int(input("Introduce otro número: "))
C= int(input("Introduce otro número: "))

x1=(-B + (B**2 - 4*A*C)**0.5) / (2*A)
x2=(-B - (B**2 - 4*A*C)**0.5) / (2*A)
print("Las soluciones son:", x1, "y", x2)

#Ten en cuenta las 3 posibles soluciones:
#- 1 solución.
#- 2 soluciones.
#- No tiene soluciones reales.



