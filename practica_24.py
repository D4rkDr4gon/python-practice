import os

# Clase Estudiante
class Estudiante:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id


# Función para ingresar un nuevo estudiante
def nuevo_estudiante():
    nombre = input("Nombre y apellido: ")
    id = input("Nuevo ID de estudiante: ")
    estudiante = Estudiante(nombre, id)
    guardar(estudiante)


# Función para guardar un estudiante en el archivo
def guardar(estudiante):
    with open("alumnos.txt", "a") as file:
        file.write(f"{estudiante.nombre},{estudiante.id}\n")
    print("Estudiante guardado exitosamente.")


# Función para leer la lista de estudiantes
def leer():
    try:
        with open("alumnos.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No se pudo abrir el archivo.")


# Bucle principal
while True:
    print("¡Bienvenido!")
    print("¿Qué desea hacer?")
    print("Nuevo alumno ==> N")
    print("Leer lista de alumnos ==> L")
    print("Finalizar el programa ==> F")
    option = input("Ingrese su opción: ")

    if option.lower() == "n":
        nuevo_estudiante()
    elif option.lower() == "l":
        leer()
    elif option.lower() == "f":
        break
    else:
        print("Opción inválida. Intente nuevamente.")

os.system("pause")
