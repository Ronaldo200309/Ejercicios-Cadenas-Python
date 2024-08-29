# Ejercicio 7
correo = input("Ingresa tu correo electrónico: ")

nombre_usuario = correo.split('@')[0]

correo_nuevo = nombre_usuario + '@ceu.es'

print(f"Tu nuevo correo electrónico es: {correo_nuevo}")
