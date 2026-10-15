#Solicita un entero N (altura del triángulo).
#Imprime un triángulo de asteriscos * disminuyendo un asterisco por fila hasta llegar a 1.
#Ejemplo para N = 4


n = int(input("escribe la altura del triangulo  "))

for i in range(n, 0, -1) :
    print("*" * i)



