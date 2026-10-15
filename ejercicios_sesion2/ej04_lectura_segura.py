"""Ejercicio 4: Lectura segura de ficheros de datos
Crea una función leer_dataset(ruta_archivo: str) -> str.
Abre y lee el contenido del archivo indicado utilizando un gestor de contexto (with open(...)).
Incluye un bloque de control de excepciones try / except para capturar el error FileNotFoundError si el archivo no existe en el disco, mostrando un aviso por pantalla en lugar de detener el programa."""


def leer_dataset(ruta_archivo: str) -> str:
    
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no se encontró.")
        return ""