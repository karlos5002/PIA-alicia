"""Ejercicio 3: Limpieza y tratamiento de datos imperfectos
Crea un DataFrame llamado productos con información de inventario que contiene registros incompletos y repetidos:

import pandas as pd
import numpy as np

productos = pd.DataFrame({
    "Producto": ["Portátil", "Ratón", "Teclado", "Monitor", "Monitor", "Portátil"],
    "Precio": [850.0, 25.0, 45.0, np.nan, 210.0, 850.0],
    "Stock": [10, 200, 150, 50, 50, 10]
})

Realiza las siguientes operaciones de limpieza de datos:

Identifica y muestra por pantalla el número total de valores nulos por columna, así como la cantidad total de filas duplicadas en el DataFrame.
Imputa (rellena) los valores ausentes en la columna Precio sustituyéndolos por el precio medio del resto de productos.
Elimina las filas duplicadas del DataFrame manteniendo solo la primera ocurrencia de cada registro.
Renombra todas las columnas para que estén escritas completamente en minúsculas (producto, precio, stock).
Convierte la columna stock a tipo flotante (float64) y muestra el DataFrame limpio final."""

import pandas as pd
import numpy as np

productos = pd.DataFrame({
"Producto": ["Portátil", "Ratón", "Teclado", "Monitor", "Monitor", "Portátil"],
"Precio": [850.0, 25.0, 45.0, np.nan, 210.0, 850.0],
"Stock": [10, 200, 150, 50, 50, 10]
})


