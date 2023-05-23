import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
respuesta = ""

while respuesta != "n":
    print("El primer dado dio un valor de:", dado1)
    print("El segundo dado dio un valor de:", dado2)
    print("La suma de ambos dados es:", dado1 + dado2)

    respuesta = input("Desea lanzar los dados nuevamente? (s/n): ")

    if respuesta == "s":
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
