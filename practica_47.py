import re

# Módulo 1: Gestor de Estudiantes

class Estudiante:
    def __init__(self, email, clave):
        self.email = email
        self.clave = clave
        self.creditos = 1000

def validar_email(email):
    patron = r'\b[A-Za-z0-9._%+-]+@frba.utn.edu.ar\b'
    return bool(re.match(patron, email))

def registrar_estudiante(estudiantes, email, clave):
    if not validar_email(email):
        print("Email no válido.")
        return

    for estudiante in estudiantes:
        if estudiante.email == email:
            print("El email ya está registrado.")
            return

    estudiantes.append(Estudiante(email, clave))
    print("Registro exitoso.")

# Módulo 2: Gestor de Beneficios y Acreditación de Logros

class Beneficio:
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo

def agregar_beneficio(beneficios, nombre, costo):
    beneficios.append(Beneficio(nombre, costo))
    print("Beneficio agregado exitosamente.")

def listar_beneficios(beneficios):
    print("Beneficios disponibles:")
    for beneficio in beneficios:
        print(f"{beneficio.nombre} - Costo: {beneficio.costo} créditos")

def acreditar_logros(estudiante, puntos):
    estudiante.creditos += puntos
    print(f"Se acreditaron {puntos} puntos. Créditos disponibles: {estudiante.creditos}")

# Módulo 3: Consumidor de Beneficios

def iniciar_sesion(estudiantes, beneficios):
    email = input("Ingrese su email: ")
    clave = input("Ingrese su clave: ")

    for estudiante in estudiantes:
        if estudiante.email == email and estudiante.clave == clave:
            print("Inicio de sesión exitoso.")
            mostrar_menu_beneficios(estudiante, beneficios)
            return

    print("Credenciales incorrectas.")

def mostrar_menu_beneficios(estudiante, beneficios):
    while True:
        print("\n--- Menú de Beneficios ---")
        print("1. Mostrar créditos disponibles")
        print("2. Mostrar beneficios disponibles")
        print("3. Consumir un beneficio")
        print("4. Acreditar logros")
        print("5. Cerrar sesión")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            print(f"Créditos disponibles: {estudiante.creditos}")
        elif opcion == '2':
            listar_beneficios(beneficios)
        elif opcion == '3':
            consumir_beneficio(estudiante, beneficios)
        elif opcion == '4':
            puntos = int(input("Ingrese la cantidad de puntos a acreditar: "))
            acreditar_logros(estudiante, puntos)
        elif opcion == '5':
            return
        else:
            print("Opción no válida. Intente nuevamente.")

def consumir_beneficio(estudiante, beneficios):
    nombre_beneficio = input("Ingrese el nombre del beneficio que desea consumir: ")

    for beneficio in beneficios:
        if beneficio.nombre == nombre_beneficio and beneficio.costo <= estudiante.creditos:
            estudiante.creditos -= beneficio.costo
            print(f"Beneficio '{nombre_beneficio}' consumido. Créditos restantes: {estudiante.creditos}")
            return

    print("No se pudo consumir el beneficio.")

# Módulo 4: Administración

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

# Función para crear una cuenta de estudiante
def crear_cuenta_estudiante(estudiantes):
    print("Crear nueva cuenta de estudiante:")
    email = input("Ingrese el email del estudiante: ")
    clave = input("Ingrese la clave del estudiante: ")

    registrar_estudiante(estudiantes, email, clave)

# Define las listas para almacenar estudiantes, beneficios y administradores
estudiantes = []
beneficios = []
administradores = []

# Agrega administradores
administradores.append(Administrador("admin1", "contraseña1"))
administradores.append(Administrador("admin2", "contraseña2"))

# Ejecuta el programa principal
while True:
    print("\n--- Menú Principal ---")
    print("1. Iniciar sesión como estudiante")
    print("2. Iniciar sesión como administrador")
    print("3. Crear cuenta de estudiante")
    print("4. Salir")

    opcion = input("Elija una opción: ")

    if opcion == '1':
        iniciar_sesion(estudiantes, beneficios)
    elif opcion == '2':
        while True:
            username = input("Ingrese el nombre de usuario del administrador: ")
            password = input("Ingrese la contraseña del administrador: ")

            if autenticar_administrador(administradores, username, password):
                print("Inicio de sesión de administrador exitoso.")
                menu_administracion(estudiantes, beneficios)
                break
            else:
                print("Credenciales de administrador incorrectas. Intente nuevamente.")
    elif opcion == '3':
        crear_cuenta_estudiante(estudiantes)
    elif opcion == '4':
        break
    else:
        print("Opción no válida. Intente nuevamente.")
