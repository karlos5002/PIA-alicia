#Solicita repetidamente una contraseña al usuario hasta que cumpla todas estas condiciones:
#Tener al menos 8 caracteres.
#Contener al menos una letra mayúscula.
#Contener al menos un número.
#Muestra un mensaje de éxito cuando la contraseña sea aceptada.


while True:
    contrasena = input("escribe una contraseña que contenga al menos 8 caracteres una letra mayuscula y al menos un numero ")
    if len(contrasena) < 8:
        print("la contraseña debe tener al menos 8 caracteres")
        continue

    if not any(c.isupper() for c in contrasena):
        print("la contraseña debe contener al menos una letra mayúscula")
        continue

    if not any(c.isdigit() for c in contrasena):
        print("la contraseña debe contener al menos un número")
        continue

    print("la contraseña es válida")
    break


