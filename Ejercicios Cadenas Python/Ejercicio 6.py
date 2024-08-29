# Ejercicio 6

frase = input("Por favor ingresa una frase: ")

vocal = input("Ingresa una vocal: ")

vocal = vocal.lower()

frase_cambiada = frase.replace(vocal, vocal.upper())

print(f"La frase con la vocal '{vocal}' en mayúscula es: {frase_cambiada}")
