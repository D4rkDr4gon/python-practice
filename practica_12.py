n = int(input("Ingrese un número: "))
suma = 0

while n > 0:
    suma += n % 10
    n //= 10

print("La suma de los dígitos es", suma)
