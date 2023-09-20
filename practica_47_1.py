import re
import pickle

class Estudiante:
    # Clase Estudiante y funciones relacionadas aquí
    def __init__(self, nombre, email, clave):
        global numero_legajo
        self.legajo = numero_legajo
        numero_legajo += 1
        self.email = email
        self.clave = clave
        self.nombre = nombre
        self.meritos = 1000

    def ver_informacion(self):
        print(f"Información del estudiante:")
        print(f"Legajo: {self.legajo}")
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Méritos disponibles: {self.meritos}")

    def modificar_informacion(self):
        print("Modificar información del estudiante:")
        print("1. Cambiar nombre")
        print("2. Cambiar contraseña")
        print("3. Salir")
        opcion = input("¿Qué desea hacer?: ")
        if opcion == '1':
            self.nombre = input("Nuevo nombre: ")
        elif opcion == '2':
            self.clave = input("Nueva clave: ")
        elif opcion == '3':
            return
        else:
            print("Opción no válida.")
        
        print("Información modificada con éxito.")


def validar_email(email):
    # Función validar_email aquí
    patron = r'\b[A-Za-z0-9._%+-]+@frba.utn.edu.ar\b'
    return bool(re.match(patron, email))

def registrar_estudiante(estudiantes):
    # Función registrar_estudiante aquí
    print("Crear nueva cuenta de estudiante:")
    nombre = input("Nombre del estudiante: ")
    email = input("Ingrese el email del estudiante: ")
    clave = input("Ingrese la clave del estudiante: ")

    if not validar_email(email):
        print("Email no válido.")
        return

    for estudiante in estudiantes:
        if estudiante.email == email:
            print("El email ya está registrado.")
            return

    estudiantes.append(Estudiante(nombre, email, clave))
    print("Registro exitoso.")

def iniciar_sesion(estudiantes):
    email = input("Ingrese su email: ")
    clave = input("Ingrese su clave: ")

    for estudiante in estudiantes:
        if estudiante.email == email and estudiante.clave == clave:
            print("Inicio de sesión exitoso.")
            menu_estudiante(estudiante, estudiantes)
            return

    print("Credenciales incorrectas.")

def menu_estudiante(estudiante, estudiantes):
    while True:
        print("\n--- Menú Estudiante ---")
        print("1. Ver mi información")
        print("2. Modificar mi información")
        print("3. Cerrar sesión")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            estudiante.ver_informacion()
        elif opcion == '2':
            estudiante.modificar_informacion()
        elif opcion == '3':
            guardar_registros(estudiantes)
            print("Sesión cerrada.")
            return
        else:
            print("Opción no válida. Intente nuevamente.")

def guardar_registros(estudiantes):
    with open("registros.dat", "wb") as registros_file:
        pickle.dump(estudiantes, registros_file)

if __name__ == "__main__":
    estudiantes = []
    numero_legajo = 1000000
    # Código principal relacionado con el Módulo 1 aquí
    while True:
        print("\n--- Menú Principal ---")
        print("1. Iniciar sesión como estudiante")
        print("2. Crear cuenta de estudiante")
        print("3. Salir")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            iniciar_sesion(estudiantes)
        elif opcion == '2':
            registrar_estudiante(estudiantes)
        elif opcion == '3':
            guardar_registros(estudiantes)
            break
        else:
            print("Opción no válida. Intente nuevamente.")
