# Ejercicio 10
productos = input("Ingresa los productos de la cesta de tu compra, separalos por comas: ")

lista_productos = productos.split(',')

print("Los productos de tu cesta de compra son:")
for producto in lista_productos:
    print(producto.strip())
