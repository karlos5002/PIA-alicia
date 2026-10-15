#Pide un número de cuenta entero de 8 dígitos.
#Muestra los primeros 4 dígitos de la cuenta.
#Calcula su dígito de control hallando el resto de dividir el número entre 11 (11−resto).
#Si el resultado es 10 pasa a ser 1, y si es 11 pasa a ser 0.


numero_cuenta=input("introduce un numero del entero de 8 digitos ")

print("Los primeros 4 dígitos son:", numero_cuenta[:4])

resto=int(numero_cuenta)%11
digito_control=11-resto

if digito_control==10:
    digito_control=1
elif digito_control==11:
    digito_control=0

print("El dígito de control es:", digito_control)