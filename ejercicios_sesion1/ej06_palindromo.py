#Solicita una palabra al usuario.
#Cuenta cuántas vocales (a, e, i, o, u) contiene la cadena.
#Comprueba si la palabra es un palíndromo
# (se lee igual de izquierda a derecha que de derecha a izquierda) e imprime el resultado.

palabra = input("introduce una palabra ")
cont=0
for letra in palabra :
    if letra == "a" :
        cont+=1
    if letra == "e" :
         cont+=1
    if letra == "i" :
        cont+=1
    if letra == "o" :
         cont+=1
    if letra == "u" :
         cont+=1

es_palindromo = palabra == palabra[::-1]


print(f"la cadena contiene: {cont} vocales")        
print(f"la palabra es un palindromo: {es_palindromo}")