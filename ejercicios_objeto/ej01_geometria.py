"""Ejercicio 1: Geometría básica de rectángulos
Crea una clase llamada Rectangulo que reciba en su constructor los atributos ancho y alto (números decimales).
Incluye un método area() que calcule y devuelva el área del rectángulo (A= ancho×alto).
Instancia dos rectángulos con dimensiones diferentes y comprueba por pantalla que el cálculo del área se realiza correctamente en ambos objetos."""

class Rectangulo:
    
    def __init__(self, ancho: float, alto: float):
        self.ancho: float = ancho
        self.alto: float = alto
        
    def area(self) -> float:
        return self.ancho * self.alto


if __name__ == "__main__":
    
    rectangulo_1 = Rectangulo(5.0, 3.0)
    
    rectangulo_2 = Rectangulo(10.5, 2.0)
    
    print(f"Área del rectángulo 1 (5x3): {rectangulo_1.area()}")
    print(f"Área del rectángulo 2 (10.5x2): {rectangulo_2.area()}")