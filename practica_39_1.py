import pickle

class Estudiante:
    def __init__(self, codigo, nombre, edad):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad

def dame_estudiante(codigo):
    nombre = input(f"Ingrese el nombre del estudiante {codigo}: ")
    edad = int(input(f"Ingrese la edad del estudiante {codigo}: "))
    return Estudiante(codigo, nombre, edad)

if __name__ == "__main__":
    estudiantes = []

    for i in range(1, 4):
        print(f"Ingrese los datos del estudiante {i}:")
        estudiantes.append(dame_estudiante(i))

    # Crear archivo binario
    with open("estudiantes_binarios.dat", "wb") as archivo:
        pickle.dump(estudiantes, archivo)

    print("Archivo creado exitosamente.")
