# Clase Alumno
class Alumno:
    def __init__(self, nombre, asig1, asig2, asig3):
        self.nombre = nombre
        self.asig1 = asig1
        self.asig2 = asig2
        self.asig3 = asig3

# Lista de alumnos
alumnos = []

# Ciclo para ingresar los datos de los alumnos
for i in range(5):
    print("Ingrese nombre:")
    nombre = input()
    print("Ingrese nota de Asignatura 1:")
    asig1 = float(input())
    print("Ingrese nota de Asignatura 2:")
    asig2 = float(input())
    print("Ingrese nota de Asignatura 3:")
    asig3 = float(input())

    # Crear objeto Alumno y agregarlo a la lista
    alumno = Alumno(nombre, asig1, asig2, asig3)
    alumnos.append(alumno)

    # Calcular promedio
    promedio = (asig1 + asig2 + asig3) / 3
    print(nombre, "tu promedio es:", promedio)

