class Camion:
    def __init__(self, matricula: str, kms_actuales: float, peso: float = 18.0, 
                 consumo: float = 20.0, capacidad_maxima: float = 200.0, 
                 combustible_actual: float = None):
        self.matricula = matricula
        self.kms_actuales = kms_actuales
        self.peso = peso
        self.consumo = consumo
        self.capacidad_maxima = capacidad_maxima
        
        if combustible_actual is None:
            self.combustible_actual = capacidad_maxima
        else:
            self.combustible_actual = combustible_actual

    def repostar_combustible(self, cantidad: float, precio_litro: float) -> float:
        espacio_disponible = self.capacidad_maxima - self.combustible_actual
        
        if espacio_disponible == 0:
            print(" Depósito lleno")
            litros_repostados = 0.0
        elif cantidad > espacio_disponible:
            litros_repostados = espacio_disponible
            self.combustible_actual = self.capacidad_maxima
        else:
            litros_repostados = cantidad
            self.combustible_actual += cantidad
            
        coste = litros_repostados * precio_litro
        print(f"Repostados {litros_repostados:.1f} L. Coste: {coste:.2f} €")
        return coste

    def calcular_km_disponibles(self) -> float:
        base_km = (self.combustible_actual / self.consumo) * 100
        
        if self.peso <= 4.5:
            penalizacion = 0
        elif self.peso <= 18.0:
            penalizacion = 50
        elif self.peso <= 25.0:
            penalizacion = 75
        else:
            penalizacion = 100
            
        km_finales = base_km - penalizacion
        
        return max(0.0, km_finales)

    def realizar_viaje(self, kms_recorrer: float) -> None:
        if kms_recorrer > self.calcular_km_disponibles():
            print("No hay suficiente combustible para este viaje.")
            return 
            
        combustible_gastado = (kms_recorrer * self.consumo) / 100
        self.combustible_actual -= combustible_gastado
        self.kms_actuales += kms_recorrer
        
        print(" Viaje realizado con éxito.")
        
        if self.calcular_km_disponibles() < 100:
            print(" El camión ha entrado en reserva (menos de 100 km disponibles).")

    def mostrar_info(self) -> None:
        print("--- Información del camión ---")
        print(f"Matrícula: {self.matricula}")
        print(f"Peso: {self.peso} t")
        print(f"Kilómetros actuales: {self.kms_actuales} km")
        print(f"Combustible actual: {self.combustible_actual} L")
        print(f"Kms disponibles: {self.calcular_km_disponibles()} km")


if __name__ == "__main__":
    c1 = Camion("1234ABC", kms_actuales=12000)
    c1.mostrar_info()
    print()

    c1.repostar_combustible(50, 1.7)
    print(f"Puede recorrer aproximadamente {c1.calcular_km_disponibles()} km.")
    print()

    c1.realizar_viaje(150)
    c1.mostrar_info()