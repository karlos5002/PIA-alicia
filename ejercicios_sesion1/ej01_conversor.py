#Pide al usuario una temperatura en grados Celsius y el precio de un producto.
#Muestra la temperatura convertida a Fahrenheit (
#(F=C×1.8+32) redondeada a 2 decimales.
#Muestra el precio final del producto tras aplicar un descuento del 15%.


print ("Bienvenido al conversor de temperatura y calculadora de descuento.")

grados_celsius= float(input("introduce unos grados celsius "))
precio_producto= float(input("introduce el precio del producto "))

fahrenheit= (grados_celsius * 1.8)+32
print(f"los grados celsius introducidos son equivalentes a {fahrenheit} fahrenheit")

precio_descuento=(precio_producto * 15) / 100
print(f"el precio introducido con el descuento añadido es de  {precio_descuento} ")
