import pickle

# ... (código anterior) ...
class Estudiante:
    numero_legajo = 1

    def __init__(self, nombre, email, clave):
        self.legajo = Estudiante.numero_legajo
        Estudiante.numero_legajo += 1
        self.email = email
        self.clave = clave
        self.nombre = nombre
        self.meritos = 1000

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
    estudiante.meritos += puntos
    print(f"Se acreditaron {puntos} puntos. Méritos disponibles: {estudiante.meritos}")

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
        print("3. Acreditar logros")
        print("4. Cerrar sesión")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            print(f"Créditos disponibles: {estudiante.meritos}")
        elif opcion == '2':
            listar_beneficios(beneficios)
        elif opcion == '3':
            puntos = int(input("Ingrese la cantidad de puntos a acreditar: "))
            acreditar_logros(estudiante, puntos)
        elif opcion == '4':
            return
        else:
            print("Opción no válida. Intente nuevamente.")


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
        print("1. Agregar beneficio")
        print("2. Salir")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del beneficio: ")
            costo = int(input("Ingrese el costo del beneficio en créditos: "))
            agregar_beneficio(beneficios, nombre, costo)
        elif opcion == '2':
            return
        else:
            print("Opción no válida. Intente nuevamente.")


def guardar_registros(estudiantes, beneficios):
    with open("registros.dat", "wb") as registros_file:
        pickle.dump((estudiantes, beneficios), registros_file)

def guardar_logros_y_beneficios(beneficios):
    with open("logrosYbeneficios.txt", "w") as logros_file:
        logros_file.write("Beneficios disponibles:\n")
        for beneficio in beneficios:
            logros_file.write(f"{beneficio.nombre} - Costo: {beneficio.costo} créditos\n")

if __name__ == "__main__":
    beneficios = []
    administradores = []
    estudiantes = []

    administradores.append(Administrador("admin1", "contraseña1"))
    administradores.append(Administrador("admin2", "contraseña2"))

    while True:
        print("\n--- Menú Principal ---")
        print("1. Iniciar sesión como estudiante")
        print("2. Iniciar sesión como administrador")
        print("3. Salir")

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
            guardar_registros(estudiantes, beneficios)
            guardar_logros_y_beneficios(beneficios)
            break
        else:
            print("Opción no válida. Intente nuevamente.")
