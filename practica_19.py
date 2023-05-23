class Alumno:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

def crear_alumno():
    nombre = input("Nombre del alumno: ")
    edad = int(input("Edad del alumno: "))
    return Alumno(nombre, edad)

def interactuar_con_alumnos():
    alumnos = []
    
    for _ in range(5):
        alumno = crear_alumno()
        alumnos.append(alumno)

    print("Lista de alumnos:")

    for alumno in alumnos:
        print(alumno.nombre, "y su edad es:", alumno.edad)

interactuar_con_alumnos()
