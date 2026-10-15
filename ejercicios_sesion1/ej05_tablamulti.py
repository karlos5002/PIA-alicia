#Pide un número entero positivo N
#Muestra su tabla de multiplicar del 1 al 10.
#Calcula la suma de todos los números enteros desde 1 hasta N e imprime el resultado total.

num = int(input("introduce un numero positivo para ver su tabla "))
sumatot =0;
for i in range(11) :
    print(i * num) 
    sumatot = i*num + sumatot

print(f"la suma total de la tabla es: {sumatot}" )    