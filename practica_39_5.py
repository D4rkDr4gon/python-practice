import pickle

class Estudiante:
    def __init__(self, codigo, nombre, edad):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad

def editar_edad_estudiante(codigo_buscado, nueva_edad):
    try:
        # Abrir el archivo binario para lectura y escritura
        with open("estudiantes_binarios.dat", "rb+") as archivo:
            estudiantes = pickle.load(archivo)
            encontrado = False

            for estudiante in estudiantes:
                if estudiante.codigo == codigo_buscado:
                    encontrado = True
                    estudiante.edad = nueva_edad
                    archivo.seek(0)  # Regresar al principio del archivo
                    pickle.dump(estudiantes, archivo)
                    print("Edad actualizada exitosamente.")
                    break

            if not encontrado:
                print("No se encontró un estudiante con ese código.")

    except FileNotFoundError:
        print("El archivo de estudiantes no se encuentra.")
    except Exception as e:
        print("Ocurrió un error al leer o escribir en el archivo:", str(e))

if __name__ == "__main__":
    codigo_buscado = int(input("Ingrese el código del estudiante a buscar: "))
    nueva_edad = int(input("Ingrese la nueva edad: "))
    editar_edad_estudiante(codigo_buscado, nueva_edad)
