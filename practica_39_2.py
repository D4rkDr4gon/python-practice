import pickle

class Estudiante:
    def __init__(self, codigo, nombre, edad):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad

def mostrar_estudiantes():
    try:
        # Abrir el archivo binario para lectura
        with open("estudiantes_binarios.dat", "rb") as archivo:
            estudiantes = pickle.load(archivo)

            for estudiante in estudiantes:
                print("Estudiante encontrado:")
                print("Código:", estudiante.codigo)
                print("Nombre:", estudiante.nombre)
                print("Edad:", estudiante.edad)
                print()

    except FileNotFoundError:
        print("El archivo de estudiantes no se encuentra.")
    except Exception as e:
        print("Ocurrió un error al leer el archivo:", str(e))

if __name__ == "__main__":
    mostrar_estudiantes()
