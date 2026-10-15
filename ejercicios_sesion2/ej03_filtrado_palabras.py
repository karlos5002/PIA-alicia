"""Ejercicio 3: Filtrado de palabras con funciones Lambda
Crea una función filtrar_palabras_largas(palabras: list[str], longitud_minima: int) -> list[str].
Utiliza una función lambda junto con la función de orden superior filter() para devolver una nueva lista únicamente con las palabras cuyo número de caracteres sea mayor que la longitud_minima."""

def filtrar_palabras_largas(palabras: list[str], longitud_minima: int) -> list[str]:
    """Filtra las palabras que tienen una longitud mayor a longitud_minima.

    Args:
        palabras (list[str]): Lista de palabras a filtrar.
        longitud_minima (int): Longitud mínima para filtrar las palabras.

    Returns:
        list[str]: Lista de palabras filtradas.
    """
    return list(filter(lambda palabra: len(palabra) > longitud_minima, palabras))






