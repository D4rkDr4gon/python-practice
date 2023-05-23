CantContacto = 1

class Contacto:
    def __init__(self, nombre, num, cod_area, correo):
        self.nombre = nombre
        self.num = num
        self.cod_area = cod_area
        self.correo = correo

def NewCont(contacto):
    if len(contacto) < CantContacto:
        nombre = input("Ingrese el Nombre: ")
        cod_area = int(input("Ingrese el código de área: "))
        num = int(input("Ingrese el número: "))
        correo = input("Ingrese el correo electrónico: ")

        nuevo_contacto = Contacto(nombre, num, cod_area, correo)
        contacto.append(nuevo_contacto)

        print("Contacto agregado exitosamente!")
    else:
        print("No hay más espacio para agregar contactos.")

def Indice(contacto, dato):
    for i in range(len(contacto)):
        if (contacto[i].cod_area == dato.cod_area or
            contacto[i].correo == dato.correo or
            contacto[i].nombre == dato.nombre or
            contacto[i].num == dato.num):
            return i

    return -1

def SearchCont(contacto):
    nombre_busqueda = input("Dato de búsqueda: ")
    dato = Contacto(nombre_busqueda, 0, 0, "")

    indice = Indice(contacto, dato)

    if indice != -1:
        print("Nombre:", contacto[indice].nombre)
        print("Número de teléfono: +{} {}".format(contacto[indice].cod_area, contacto[indice].num))
        print("Correo electrónico:", contacto[indice].correo)
    else:
        print("No se encontró el dato.")

def PrintCont(contacto):
    print("Lista de contactos:")

    for i in range(len(contacto)):
        print("Nombre:", contacto[i].nombre)
        print("Número de teléfono: +{} {}".format(contacto[i].cod_area, contacto[i].num))
        print("Correo electrónico:", contacto[i].correo)

def DeleteCont(contacto):
    nombre_borrar = input("Nombre del contacto a borrar: ")
    dato = Contacto(nombre_borrar, 0, 0, "")

    indice = Indice(contacto, dato)

    if indice != -1:
        contacto.pop(indice)
        print("Se ha borrado el contacto.")
    else:
        print("No se encontró el contacto.")

contacto = []

print("¡Bienvenido a la libreta de contactos!")

while True:
    print("--------------------------------------")
    print("¿Qué desea hacer?")
    print("N --> Nuevo contacto")
    print("B --> Buscar contacto")
    print("M --> Mostrar la libreta entera")
    print("D --> Borrar un contacto")
    print("Q --> Finalizar el programa")
    eleccion = input().lower()
    print("--------------------------------------")

    if eleccion == 'n':
        NewCont(contacto)
    elif eleccion == 'b':
        SearchCont(contacto)
    elif eleccion == 'm':
        PrintCont(contacto)
    elif eleccion == 'd':
        DeleteCont(contacto)
    elif eleccion == 'q':
        print("¡Hasta la próxima!")
        break
