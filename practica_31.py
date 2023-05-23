class Tarea:
    def __init__(self, nombre, descripcion, progreso):
        self.nombre = nombre
        self.descripcion = descripcion
        self.progreso = progreso

def Create(gestor):
    tarea = Tarea("", "", "en progreso")
    print("----- Nueva Tarea -----")
    tarea.nombre = input("Ingrese el título de la tarea: ")
    tarea.descripcion = input("Ingrese una breve descripción: ")

    gestor.append(tarea)
    print("Tarea creada exitosamente!")

def Mostrar(gestor):
    for tarea in gestor:
        print("----- TAREA -----")
        print("Título:", tarea.nombre)
        print("Descripción:", tarea.descripcion)
        print("Estado:", tarea.progreso)

def Progreso(gestor):
    nombre_tarea = input("Ingrese el nombre de la tarea: ")
    for tarea in gestor:
        if tarea.nombre == nombre_tarea:
            tarea.progreso = "completado"
            print("Progreso de la tarea actualizado.")
            return
    print("No se encontró la tarea.")

gestor = []

print("¡Bienvenido al gestor de tareas!")

while True:
    print("---------------------------------")
    print("¿Qué deseas hacer?")
    print("C = Crear tarea")
    print("M = Mostrar tareas")
    print("P = Registrar tarea completada")
    print("Q = Salir del programa")
    option = input().lower()
    print("---------------------------------")

    if option == 'c':
        Create(gestor)
    elif option == 'p':
        Progreso(gestor)
    elif option == 'm':
        Mostrar(gestor)
    elif option == 'q':
        print("¡Fin del programa!")
        break
    else:
        print("Opción no válida.")

