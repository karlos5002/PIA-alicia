"""Ejercicio 2: Analizador estadístico con parámetros variables
Crea una función analizar_numeros(*numeros: float) -> dict.
La función debe aceptar cualquier cantidad de números como argumentos posicionales y devolver un diccionario con:
La cantidad total de números recibidos.
La suma total.s
El valor máximo y mínimo.
La media aritmética.
Maneja mediante un condicional el caso en que no se reciba ningún número para evitar errores de división entre cero."""

def analizar_numeros(*numeros: float) -> dict:
    if len(numeros) == 0:
        return {
            "cantidad": 0,
            "suma": 0.0,
            "maximo": None,
            "minimo": None,
            "media": 0.0
        }
    
    cantidad = len(numeros)
    suma_total = sum(numeros)
    
    return {
        "cantidad": cantidad,
        "suma": suma_total,
        "maximo": max(numeros),
        "minimo": min(numeros),
        "media": suma_total / cantidad
    }


