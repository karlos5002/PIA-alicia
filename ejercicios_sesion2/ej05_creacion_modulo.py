"""Ejercicio 5: Creación de un módulo propio y punto de entrada principal
Crea un módulo llamado utilidades_texto.py con dos funciones tipadas:
limpiar_prompt(texto: str) -> str: elimina los espacios sobrantes en los extremos y convierte el texto a minúsculas.
contar_palabras(texto: str) -> int: devuelve la cantidad total de palabras de la frase.
Crea un segundo archivo llamado main.py en el mismo directorio. Importa el módulo utilidades_texto y utiliza ambas funciones para procesar una frase introducida por el usuario.
Comprobación experimental:
Añade un mensaje print() de prueba al final de utilidades_texto.py fuera de cualquier función y sin usar if __name__ == "__main__":. Ejecuta main.py y observa cómo ese mensaje de prueba se imprime automáticamente al importar el módulo.
Envuelve dicho código de prueba dentro del bloque if __name__ == "__main__": en utilidades_texto.py. Vuelve a ejecutar main.py y comprueba que ahora las pruebas locales del módulo ya NO se ejecutan al importar la librería desde main.py.
"""

