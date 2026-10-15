"""
Ejercicio 1: Conversor de escalas de temperatura
Crea una función convertir_temperatura(valor: float, escala_origen: str, escala_destino: str) -> float.
Permite convertir entre Celsius ("C"), Fahrenheit ("F") y Kelvin ("K").
Si se introduce una escala que no existe, la función debe lanzar una excepción ValueError informando al usuario."""

def convertir_temperatura(valor: float, escala_origen: str, escala_destino: str) -> float:

    origen = escala_origen.upper()
    destino = escala_destino.upper()
    
    escalas_validas = ["C", "F", "K"]
    
    if origen not in escalas_validas or destino not in escalas_validas:
        raise ValueError(f"Escala incorrecta. Usa 'C', 'F' o 'K'. Has introducido: {escala_origen} a {escala_destino}")
    
    if origen == destino:
        return valor
        
    if origen == "C":
        if destino == "F":
            return (valor * 9/5) + 32
        elif destino == "K":
            return valor + 273.15
            
    elif origen == "F":
        if destino == "C":
            return (valor - 32) * 5/9
        elif destino == "K":
            return (valor - 32) * 5/9 + 273.15
            
    elif origen == "K":
        if destino == "C":
            return valor - 273.15
        elif destino == "F":
            return (valor - 273.15) * 9/5 + 32
