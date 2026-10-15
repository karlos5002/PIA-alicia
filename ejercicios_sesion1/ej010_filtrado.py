#Pide al usuario un umbral de confianza (ejemplo: 0.75).
#Solicita repetidamente puntuaciones de probabilidad (números decimales entre 0.0 y 1.0) hasta que se introduzca la palabra "fin".
#Para cada valor introducido, indica si la predicción es "Aceptada" (mayor o igual al umbral) o "Rechazada".

umbral = float(input("Introduce un umbral de confianza: "))

while True:
    entrada = input("Introduce una puntuación de probabilidad o fin para acabar: ")
    if entrada == "fin":
        break
    probabilidad = float(entrada)
    if probabilidad >= umbral:
        print("aceptada")
    else:
        print("rechazada")