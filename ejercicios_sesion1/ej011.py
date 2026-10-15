#Solicita una frase de entrada simulando un prompt para un modelo de lenguaje (LLM).
#Limpia los espacios innecesarios al inicio y al final, reemplaza los tabuladores por espacios simples y comprueba si el texto supera los 50 caracteres para mostrar una advertencia de longitud.

frase = input("Introduce una frase: ")
frase_limpia = frase.strip().replace("\t", " ")

if len(frase_limpia) > 50:
 print("Advertencia: la frase supera los 50 caracteres.")    

print("Frase limpia:", frase_limpia)
