#10.- sumatorio       
#Realiza un programa que calcule el sumatorio de un número. 
#Ej Sumatorio(6)=6+5+4+3+2+1+0=21

numero = int(input("Introduce un número: "))
suma = 0

for i in range(1, numero + 1):
    suma = suma + i

print("El sumatorio es:", suma)
