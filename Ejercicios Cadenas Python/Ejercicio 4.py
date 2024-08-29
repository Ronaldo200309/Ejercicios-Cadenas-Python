# Ejercicio 4

telefono = input("Ingresa un número de teléfono en formato +34-número-extensión,por favor: ")

partes = telefono.split('-')

numero_telefono = partes[1]

print(f"Tu número de teléfono sin prefijo ni extensión es: {numero_telefono}")
