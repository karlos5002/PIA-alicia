"""Ejercicio 2: Indexación, selección y cálculo de nuevas características
Tomando como base el DataFrame empleados del ejercicio anterior:

Accede y muestra de forma individual el salario asignado a la empleada Marta.
Muestra las dos primeras filas del DataFrame empleando selección por posición o etiqueta.
Añade una nueva columna calculada llamada Bonus cuyo valor corresponda al 10% del salario de cada trabajador.
Muestra el DataFrame con la nueva columna añadida.
Elimina la columna Bonus del DataFrame y comprueba que la estructura vuelve a su estado original."""

import pandas as pd

if __name__ == "__main__":
    
    datos = {
        "Nombre": ["Ana", "Luis", "Marta", "Jorge", "Sara"],
        "Edad": [28, 35, 40, 30, 27],
        "Departamento": ["Ventas", "IT", "RRHH", "IT", "Ventas"],
        "Salario": [2300, 2800, 3000, 2500, 2200]
    }
    empleados = pd.DataFrame(datos)
    
    
    salario_marta = empleados.loc[empleados["Nombre"] == "Marta", "Salario"].values[0]
    
    print("--- salario individual ---")
    print(f"El salario de Marta es: {salario_marta}€")
    
   
    primeras_filas = empleados.iloc[:2]
    
    print("\n--- dos primeras filas ---")
    print(primeras_filas)
    
    
    empleados["Bonus"] = empleados["Salario"] * 0.10
    
    print("\n--- datos con bonus ---")
    print(empleados)
    
    
    empleados = empleados.drop("Bonus", axis=1)
    
    print("\n--- datos reestablecidos ---")
    print(empleados)