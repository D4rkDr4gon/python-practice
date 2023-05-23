import sys

i = int(input("Ingrese el tamaño del arreglo: "))

# Crear una lista de enteros
numeros = [0] * i

# Calcular el tamaño en bytes
size = sys.getsizeof(numeros)
print("El tamaño del arreglo es:", size, "bytes")
