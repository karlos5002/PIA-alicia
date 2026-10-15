"""Ejercicio 2: Indexación, slicing bidimensional y vistas en memoria
Crea una matriz de 4 filas por 5 columnas que contenga los números enteros del 1 al 20 ordenados secuencialmente.
Extrae y muestra por pantalla las siguientes selecciones:
El elemento ubicado en la tercera fila y cuarta columna.
La submatriz central de 2 filas por 3 columnas (filas de la 1 a la 2 y columnas de la 1 a la 3).
La última columna completa de la matriz original.
Modifica la submatriz central asignando el valor 0 a todos sus elementos y comprueba mediante una impresión por pantalla que los cambios se reflejan en la matriz original (demostrando el concepto de view o vista)."""

import numpy as np

if __name__ == "__main__":
    

    matriz = np.arange(1, 21).reshape(4, 5)
    
    print("--- MATRIZ ORIGINAL ---")
    print(matriz)

    elemento = matriz[2, 3]
    print(f"\na) Elemento (3ª fila, 4ª columna): {elemento}") 
    
    submatriz = matriz[1:3, 1:4]
    print("\nb) Submatriz central:")
    print(submatriz)
  

    ultima_columna = matriz[:, -1]
    print(f"\nc) Última columna: {ultima_columna}")

    print("\n--- EL PELIGRO DE LAS VISTAS ---")
    
    submatriz[:] = 0 
    print("Submatriz modificada a ceros:")
    print(submatriz)
    
    print("\nMatriz original tras el cambio:")
    print(matriz)