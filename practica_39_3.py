import pickle

class Estudiante:
    def __init__(self, codigo, nombre, edad):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad

def buscar_estudiante(nombre_buscado):
    try:
        # Abrir el archivo binario para lectura
        with open("estudiantes_binarios.dat", "rb") as archivo:
            estudiantes = pickle.load(archivo)

            for estudiante in estudiantes:
                if estudiante.nombre == nombre_buscado:
                    print("Estudiante encontrado:")
                    print("Código:", estudiante.codigo)
                    print("Nombre:", estudiante.nombre)
                    print("Edad:", estudiante.edad)
                    return 1

        print("Estudiante no encontrado.")
        return 0

    except FileNotFoundError:
        print("El archivo de estudiantes no se encuentra.")
        return 0
    except Exception as e:
        print("Ocurrió un error al leer el archivo:", str(e))
        return 0

if __name__ == "__main__":
    nombre = input("Ingrese el nombre del estudiante a buscar: ")
    buscar_estudiante(nombre)
