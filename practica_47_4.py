import pickle
import re

class Estudiante:
    numero_legajo = 1

    def __init__(self, nombre, email, clave):
        self.legajo = Estudiante.numero_legajo
        Estudiante.numero_legajo += 1
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
        opcion = input("¿Qué desea hacer? (1/2/3): ")
        if opcion == '1':
            self.nombre = input("Nuevo nombre: ")
        elif opcion == '2':
            self.clave = input("Nueva clave: ")
        elif opcion == '3':
            return
        else:
            print("Opción no válida. Intente nuevamente.")

class Beneficio:
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo

def agregar_beneficio(beneficios, nombre, costo):
    beneficios.append(Beneficio(nombre, costo))
    print("Beneficio agregado exitosamente.")

class Administrador:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def autenticar_administrador(administradores, username, password):
    for admin in administradores:
        if admin.username == username and admin.password == password:
            return True
    return False

def menu_administracion(estudiantes, beneficios):
    while True:
        print("\n--- Menú de Administración ---")
        print("1. Modificar datos de estudiante")
        print("2. Agregar beneficio")
        print("3. Crear cuenta de estudiante")
        print("4. Salir")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            modificar_datos_estudiante(estudiantes)
        elif opcion == '2':
            nombre = input("Ingrese el nombre del beneficio: ")
            costo = int(input("Ingrese el costo del beneficio en créditos: "))
            agregar_beneficio(beneficios, nombre, costo)
        elif opcion == '3':
            crear_cuenta_estudiante(estudiantes)
        elif opcion == '4':
            return
        else:
            print("Opción no válida. Intente nuevamente.")

def modificar_datos_estudiante(estudiantes):
    email = input("Ingrese el email del estudiante cuyos datos desea modificar: ")

    for estudiante in estudiantes:
        if estudiante.email == email:
            nueva_clave = input("Ingrese la nueva clave para el estudiante: ")
            estudiante.clave = nueva_clave
            print("Datos del estudiante actualizados.")
            return

    print("Estudiante no encontrado.")

def ver_informacion_estudiante(estudiantes, email):
    for estudiante in estudiantes:
        if estudiante.email == email:
            estudiante.ver_informacion()
            return

def crear_cuenta_estudiante(estudiantes):
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

def validar_email(email):
    # Función para validar el formato de un email
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def guardar_registros(estudiantes, beneficios):
    with open("registros.dat", "wb") as registros_file:
        pickle.dump((estudiantes, beneficios), registros_file)

def guardar_logros_y_beneficios(beneficios):
    with open("logrosYbeneficios.txt", "w") as logros_file:
        logros_file.write("Beneficios disponibles:\n")
        for beneficio in beneficios:
            logros_file.write(f"{beneficio.nombre} - Costo: {beneficio.costo} créditos\n")

if __name__ == "__main__":
    administradores = []
    estudiantes = []
    beneficios = []
    numero_legajo = 1000000

    administradores.append(Administrador("admin1", "contraseña1"))
    administradores.append(Administrador("admin2", "contraseña2"))

    while True:
        print("\n--- Menú Principal ---")
        print("1. Iniciar sesión como administrador")
        print("2. Salir")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            while True:
                username = input("Ingrese el nombre de usuario del administrador: ")
                password = input("Ingrese la contraseña del administrador: ")

                if autenticar_administrador(administradores, username, password):
                    print("Inicio de sesión de administrador exitoso.")
                    menu_administracion(estudiantes, beneficios)
                    break
                else:
                    print("Credenciales de administrador incorrectas. Intente nuevamente.")
        elif opcion == '2':
            guardar_registros(estudiantes, beneficios)
            guardar_logros_y_beneficios(beneficios)
            break
        else:
            print("Opción no válida. Intente nuevamente.")
