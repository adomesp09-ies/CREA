#Realiza un programa en pyhton que tome números de entrada hasta que le des 0. 
# A continuación debe mostrar el número de pares, impares, positivos y negativos. 
# El 0 no cuenta
pos = 0
neg = 0
par = 0
imp = 0
n = int(input("Introduce un número: "))

while n != 0:
    if n > 0:
            pos = pos + 1
    if n < 0:
         neg = neg + 1              
    if n % 2 == 0:
        par = par + 1
    else:
        imp = imp + 1      
    n = int(input("Introduce otro número: "))
print("Num POS:", pos, "Num NEG:", neg, "Num PAR:", par, "Num IMP:", imp)
                                            