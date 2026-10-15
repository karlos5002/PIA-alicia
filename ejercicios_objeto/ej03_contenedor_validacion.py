"""Ejercicio 3: Contenedor y validación de datos para experimentos (Dataset)
Crea una clase llamada Dataset para almacenar y analizar medidas o lecturas numéricas de experimentos.
El constructor debe recibir una lista inicial de valores (por defecto vacía). En el constructor se debe verificar que todos los elementos sean de tipo numérico (int o float). Si la lista contiene elementos de otro tipo (cadenas, booleanos, etc.), se debe mostrar un aviso por pantalla e inicializar la lista de datos como vacía.
Implementa los siguientes métodos:
agregar_dato(valor: float): añade un nuevo número a la lista tras verificar que es de tipo numérico.
resumen(): calcula y devuelve en una tupla la media aritmética, el valor mínimo y el valor máximo. Si la lista está vacía, debe indicarlo mediante un mensaje adecuado.
total_muestras(): devuelve la cantidad total de lecturas guardadas."""

class Dataset:
    def __init__(self, valores_iniciales: list = None):
        if valores_iniciales is None:
            valores_iniciales = []
            
        self.datos: list = []
        
        son_numeros = all(isinstance(v, (int, float)) for v in valores_iniciales)
        
        if not son_numeros and len(valores_iniciales) > 0:
            print("La lista contiene elementos no numéricos. Inicializando lista vacía.")
            self.datos = []
        else:
            self.datos = valores_iniciales.copy()

    def agregar_dato(self, valor: float) -> None:
        if isinstance(valor, (int, float)):
            self.datos.append(valor)
        else:
            print(f"El valor '{valor}' no es numérico y no se ha añadido.")

    def resumen(self) -> tuple:
        if len(self.datos) == 0:
            print("El dataset está vacío. No hay resumen.")
            return (0.0, 0.0, 0.0)
            
        media = sum(self.datos) / len(self.datos)
        minimo = min(self.datos)
        maximo = max(self.datos)
        
        return (media, minimo, maximo)

    # 4. Conteo de lecturas
    def total_muestras(self) -> int:
        return len(self.datos)


if __name__ == "__main__":
    
    print("--- Dataset Válido ---")
    experimento = Dataset([12.5, 14.1, 10.2])
    experimento.agregar_dato(13.8)
    
    print(f"Total muestras: {experimento.total_muestras()}")
    
    med, m_min, m_max = experimento.resumen()
    print(f"Media: {med:.2f} | Mín: {m_min} | Máx: {m_max}")
    
    print("\n--- Dataset Inválido ---")
    experimento_roto = Dataset([10.5, "texto", 8.2]) 
    print(f"Muestras tras el error: {experimento_roto.total_muestras()}")