"""Ejercicio 2: Gestión de cuenta bancaria con saldo protegido
Crea una clase llamada CuentaBancaria con los atributos titular (texto) y saldo (número decimal, con valor por defecto de 100.0 si no se especifica).
Implementa los siguientes métodos:
depositar(cantidad: float): suma la cantidad indicada al saldo de la cuenta.
retirar(cantidad: float): resta la cantidad del saldo. Si se intenta retirar una cantidad superior al saldo disponible, debe lanzar una excepción ValueError informando que no se puede dejar la cuenta en números negativos.
mostrar_saldo(): imprime por pantalla el titular y el saldo actual de la cuenta."""

class CuentaBancaria:
    
    def __init__(self, titular: str, saldo: float = 100.0):
        self.titular: str = titular
        self.saldo: float = saldo
        
    def depositar(self, cantidad: float):
        self.saldo += cantidad
        
    def retirar(self, cantidad: float):
        if cantidad > self.saldo:
            raise ValueError("No se puede dejar la cuenta en números negativos.")
        self.saldo -= cantidad
        
    def mostrar_saldo(self):
        print(f"Titular: {self.titular}, Saldo actual: {self.saldo:.2f}")

if __name__ == "__main__":
    cuenta = CuentaBancaria("Juan Pérez")
    cuenta.mostrar_saldo()
    
    cuenta.depositar(50.0)
    cuenta.mostrar_saldo()
    
    try:
        cuenta.retirar(200.0)
    except ValueError as e:
        print(e)
    
    cuenta.retirar(30.0)
    cuenta.mostrar_saldo()
    