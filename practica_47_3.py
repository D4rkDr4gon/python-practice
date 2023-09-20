import pickle

class Estudiante:
    numero_legajo = 1

    def __init__(self, nombre, email, clave):
        self.legajo = Estudiante.numero_legajo
        Estudiante.numero_legajo += 1
        self.email = email
        self.clave = clave
        self.nombre = nombre
        self.meritos = 1000

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
        print("2. Consumir un beneficio")
        print("3. Cerrar sesión")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            print(f"Créditos disponibles: {estudiante.meritos}")
        elif opcion == '2':
            consumir_beneficio(estudiante, beneficios)
        elif opcion == '3':
            return
        else:
            print("Opción no válida. Intente nuevamente.")

def consumir_beneficio(estudiante, beneficios):
    nombre_beneficio = input("Ingrese el nombre del beneficio que desea consumir: ")

    for beneficio in beneficios:
        if beneficio.nombre == nombre_beneficio and beneficio.costo <= estudiante.meritos:
            estudiante.meritos -= beneficio.costo
            print(f"Beneficio '{nombre_beneficio}' consumido. Créditos restantes: {estudiante.meritos}")
            return

    print("No se pudo consumir el beneficio.")

def guardar_registros(estudiantes, beneficios):
    with open("registros.dat", "wb") as registros_file:
        pickle.dump((estudiantes, beneficios), registros_file)

def guardar_logros_y_beneficios(beneficios):
    with open("logrosYbeneficios.txt", "w") as logros_file:
        logros_file.write("Beneficios disponibles:\n")
        for beneficio in beneficios:
            logros_file.write(f"{beneficio.nombre} - Costo: {beneficio.costo} créditos\n")

if __name__ == "__main__":
    estudiantes = []
    beneficios = []

    while True:
        print("\n--- Menú Principal ---")
        print("1. Iniciar sesión como estudiante")
        print("2. Salir")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            iniciar_sesion(estudiantes, beneficios)
        elif opcion == '2':
            guardar_registros(estudiantes, beneficios)
            guardar_logros_y_beneficios(beneficios)
            break
        else:
            print("Opción no válida. Intente nuevamente.")
