# Ejercicio 3
nombre = input("Ingresa tu nombre: ")

nombre_mayusculas = nombre.upper()

numero_letras = len(nombre.replace(" ", ""))

print(f"{nombre_mayusculas} tiene {numero_letras} letras")
