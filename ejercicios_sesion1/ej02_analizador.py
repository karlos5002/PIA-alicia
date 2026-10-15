#Solicita al usuario su nombre completo y la dirección URL de un sitio web.
#Muestra el nombre en mayúsculas, en minúsculas y la cantidad total de caracteres.
#Comprueba si la URL comienza por "https://" e imprime True o False.
print ("Bienvenido al analizador de texto.")

Nombre_completo= input("introduce tu nombre completo ")
URL= input("introduce la URL de un sitio web ")

print(f"El nombre en mayúsculas es: {Nombre_completo.upper()}")
print(f"El nombre en minúsculas es: {Nombre_completo.lower()}")
print(f"La cantidad total de caracteres es: {len(Nombre_completo)}")

print(f"La URL comienza por 'https://': {URL.startswith('https://')}")
