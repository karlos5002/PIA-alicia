"""Ejercicio 3: Operaciones vectorizadas y filtrado booleano
Crea un array unidimensional con 15 temperaturas simuladas (valores flotantes comprendidos entre 15.0 y 40.0 grados Celsius).
Convierte todas las temperaturas a grados Fahrenheit mediante una operación vectorizada (F=C×1.8+32F).
Utiliza indexación booleana para extraer en un nuevo array únicamente las temperaturas en Celsius estrictamente superiores a 30.0 grados.
Aplica un umbral (thresholding) sobre el array original sustituyendo cualquier valor superior a 35.0 grados por el límite máximo 35.0.+"""

import numpy as np

if __name__ == "__main__":
    temperaturas_celsius = np.random.uniform(15.0, 40.0, 15)
    print("Temperaturas en Celsius:")
    print(temperaturas_celsius)

    temperaturas_fahrenheit = temperaturas_celsius * 1.8 + 32
    print("\nTemperaturas en Fahrenheit:")
    print(temperaturas_fahrenheit)

    temperaturas_filtradas = temperaturas_celsius[temperaturas_celsius > 30.0]
    print("\nTemperaturas en Celsius superiores a 30.0:")
    print(temperaturas_filtradas)

    temperaturas_original = np.copy(temperaturas_celsius)
    temperaturas_original[temperaturas_original > 35.0] = 35.0
    print("\nTemperaturas originales con umbral aplicado:")
    print(temperaturas_original)
