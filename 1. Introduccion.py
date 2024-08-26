print("******* Introducción a Python *********");

# Definir la lista
lista = [1, 2, 3, 4, 5]

# Aplicar la función map para obtener los cuadrados
cuadrado = list(map(lambda x: x**2, lista))

# Mostrar las listas
print("Lista: ", lista)
print("Lista al cuadrado: ", cuadrado)

# Recorrer y mostrar los elementos de la lista al cuadrado
for elemento in cuadrado:
    print(elemento)
