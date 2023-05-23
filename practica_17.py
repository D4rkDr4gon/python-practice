import random

def juego_adivinanza():
    random.seed()                            # Inicializar semilla para la generación de números aleatorios
    numero_aleatorio = random.randint(1, 1000)  # Generar número aleatorio entre 1 y 1000
    intentos = 0

    print("Bienvenido al juego de adivinanza")
    print("Tienes que adivinar un número entre 1 y 1000")

    while True:
        numero_usuario = int(input("Introduce un número: "))
        intentos += 1

        if numero_usuario > numero_aleatorio:
            print("El número es menor")
        elif numero_usuario < numero_aleatorio:
            print("El número es mayor")
        else:
            print(f"¡Adivinaste el número en {intentos} intentos!")
            break

juego_adivinanza()
