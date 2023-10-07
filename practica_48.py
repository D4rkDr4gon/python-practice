class Cancion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntuacion = 0

class NodoCanciones:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None

def crear_nodo(valor):
    return NodoCanciones(Cancion(valor))

def cargar_historial(inicio, valor):
    nuevo_nodo = crear_nodo(valor.nombre)
    nuevo_nodo.cancion.puntuacion = valor.puntuacion

    if inicio is None:
        inicio = nuevo_nodo
    else:
        actual = inicio
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    return inicio

def imprimir_historial(inicio):
    actual = inicio
    while actual is not None:
        print(f'{actual.cancion.nombre} {actual.cancion.puntuacion}')
        actual = actual.siguiente

def buscar_cancion_puntuada(inicio, puntuacion):
    actual = inicio
    while actual is not None:
        if actual.cancion.puntuacion == puntuacion:
            return actual
        actual = actual.siguiente
    return None

def buscar_cancion_nombre(inicio, nombre):
    actual = inicio
    while actual is not None:
        if actual.cancion.nombre == nombre:
            return actual
        actual = actual.siguiente
    return None

def push(pila, valor):
    nuevo_nodo = crear_nodo(valor)
    nuevo_nodo.siguiente = pila
    pila = nuevo_nodo
    return pila

def pop(pila):
    if pila is None:
        print("La playlist está vacía.")
        return pila, ""

    valor = pila.cancion.nombre
    temp = pila
    pila = pila.siguiente
    del temp
    return pila, valor

def is_empty(pila):
    return pila is None

def reproducir(pila, historial):
    if is_empty(pila):
        print("La playlist está vacía.")
        return pila

    proxima_cancion, pila = pop(pila)
    print(f"La canción que se reproduce es: {proxima_cancion}")
    puntuacion = input("Puntuar la canción (1* - 5*): ")

    # Verificar que la puntuación esté en el rango válido (1-5)
    if puntuacion.isdigit() and 1 <= int(puntuacion) <= 5:
        historial = cargar_historial(historial, Cancion(proxima_cancion, int(puntuacion)))
    else:
        print("Puntuación no válida. La canción no será puntuada.")

    return pila, historial

def mostrar(pila):
    if is_empty(pila):
        print("La playlist está vacía.")
    else:
        print(f"La próxima canción es: {pila.cancion.nombre}")

def inversor(pila):
    pila_aux = None
    while not is_empty(pila):
        valor, pila = pop(pila)
        pila_aux = push(pila_aux, valor)
    return pila_aux

pila = None
historial = None

while True:
    print("-------Spotify----------")
    print("Tu playlist:")
    print("1. Agregar Cancion")
    print("2. Eliminar la primera cancion")
    print("3. Tomar cancion para reproducir")
    print("4. Invertir la playlist")
    print("5. Ver historial de reproduccion")
    print("6. Buscar las canciones previamente puntuadas")
    print("7. Buscar las canciones por nombre")
    print("8. Salir")
    opcion = input("¿Qué desea hacer? ")

    if opcion == "1":
        cancion = input("Nombre de la canción: ")
        pila = push(pila, cancion)
        print(f"{cancion} añadida con éxito.")
    elif opcion == "2":
        pila, _ = pop(pila)
        print("Primera canción eliminada.")
    elif opcion == "3":
        print("------Panel de reproducción-------")
        pila, historial = reproducir(pila, historial)
        mostrar(pila)
    elif opcion == "4":
        pila = inversor(pila)
        print("Playlist invertida.")
    elif opcion == "5":
        imprimir_historial(historial)
    elif opcion == "6":
        print("----- Búsqueda en función de puntuación -----")
        puntuacion = input("Ingrese la cantidad de estrellas: ")
        buscar_cancion_puntuada(historial, int(puntuacion))
    elif opcion == "7":
        print("----- Búsqueda en función de nombre -----")
        nombre = input("Ingrese el nombre de la canción: ")
        buscar_cancion_nombre(historial, nombre)
    elif opcion == "8":
        print("Reproducción terminada.")
        break
    else:
        print("Opción inválida.")
