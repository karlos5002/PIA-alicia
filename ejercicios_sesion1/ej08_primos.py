#Solicita un número entero mayor que 1.
#Determina e indica si el número es primo (divisible únicamente por 1 y por sí mismo).

num = input("escribe un numero entero mayor que 1 ")
num = int(num)

if num <= 1:
    print("el número debe ser mayor que 1")
else:
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break

    if es_primo:
        print(f"el número {num} es primo")
    else:
        print(f"el número {num} no es primo")

            