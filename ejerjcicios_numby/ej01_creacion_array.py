"""Ejercicio 1: Creación e inspección de arrays
Crea un vector unidimensional con números enteros del 10 al 50 (ambos inclusive) distribuidos a intervalos de 5 en 5.
Crea una matriz bidimensional de ceros de 3 filas por 4 columnas con tipo de dato flotante (float) y modifica la segunda fila completa para que contenga únicamente unos.
Genera una matriz de 4 filas por 3 columnas rellena con números enteros aleatorios entre 1 y 20.
Imprime por pantalla cada uno de los arrays junto con sus propiedades principales: forma (shape), número de dimensiones (ndim) y tipo de dato (dtype)."""

import numpy as np

vector = np.arange(10, 51, 5)

matriz = np.zeros((3, 4), dtype=np.float64)
matriz[1] = 1

matriz_aleatoria = np.random.randint(1, 21, (4, 3))

print("Vector:")
print(vector)
print("Forma:", vector.shape)
print("Número de dimensiones:", vector.ndim)
print("Tipo de dato:", vector.dtype)

print("\nMatriz:")
print(matriz)
print("Forma:", matriz.shape)
print("Número de dimensiones:", matriz.ndim)
print("Tipo de dato:", matriz.dtype)

print("\nMatriz aleatoria:")
print(matriz_aleatoria)
print("Forma:", matriz_aleatoria.shape)
print("Número de dimensiones:", matriz_aleatoria.ndim)
print("Tipo de dato:", matriz_aleatoria.dtype)
