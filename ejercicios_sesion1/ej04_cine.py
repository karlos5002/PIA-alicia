#El precio estándar de una entrada es de 8€.
#El precio se reduce a 5€ si cumple al menos una de estas condiciones
# : es miércoles, el usuario es menor de 12 años o mayor de 65 años.
#Pide al usuario su edad y el día de la semana, e indica el precio final a pagar.

edad = int(input("Introduzca su edad "))
dia = input("introduzca el dia de la semana ")

if (edad < 12) or (edad > 65) :
    print("su entrada tiene costo reducido de 8 a 5€")

elif dia == "miercoles":
    print("su entrada tiene costo reducido de 8 a 5€")
