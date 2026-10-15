"""Ejercicio 1: Creación, exploración y tipado de un DataFrame
Crea un DataFrame llamado empleados a partir de la siguiente información:

Nombre	Edad	Departamento	Salario
Ana	28	Ventas	2300
Luis	35	IT	2800
Marta	40	RRHH	3000
Jorge	30	IT	2500
Sara	27	Ventas	2200
A partir de este conjunto de datos:

Muestra por pantalla las 3 primeras filas del DataFrame y consulta su resumen informativo con los métodos correspondientes.
Imprime los tipos de datos asignados a cada columna.
Convierte el tipo de dato de la columna Edad a un formato entero más eficiente (int32) y comprueba el cambio.
Selecciona y muestra en una nueva vista únicamente las columnas Nombre y Salario.
Filtra y muestra únicamente los empleados que pertenecen al departamento "IT"."""

import pandas as pd

if __name__ == "__main__":
    
    datos = {
        "Nombre": ["Ana", "Luis", "Marta", "Jorge", "Sara"],
        "Edad": [28, 35, 40, 30, 27],
        "Departamento": ["Ventas", "IT", "RRHH", "IT", "Ventas"],
        "Salario": [2300, 2800, 3000, 2500, 2200]
    }
    
    empleados = pd.DataFrame(datos)
    
    print("--- 3 PRIMERAS FILAS ---")
    print(empleados.head(3))
    
    print("\n--- RESUMEN  ---")
    empleados.info() 
    
    print("\n--- TIPOS DE DATOS ORIGINALES ---")
    print(empleados.dtypes)
    
   
    empleados["Edad"] = empleados["Edad"].astype("int32")
    
    print("\n--- TIPOS DE DATOS TRAS EL CAMBIO ---")
    print(empleados.dtypes)
    
    
    vista_salarios = empleados[["Nombre", "Salario"]]
    print("\n--- VISTA: NOMBRE Y SALARIO ---")
    print(vista_salarios)
    
  
    empleados_it = empleados[empleados["Departamento"] == "IT"]
    print("\n--- EMPLEADOS DE IT ---")
    print(empleados_it)