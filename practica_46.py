# Definición de la clase Nodo para listas enlazadas simples
class Nodo:
    def __init__(self, valor):
        self.dato = valor
        self.siguiente = None

# Función para imprimir una lista enlazada simple
def imprimirListaSimple(inicio):
    actual = inicio
    while actual is not None:
        print(actual.dato, end=" ")
        actual = actual.siguiente
    print()

# Crear una lista enlazada simple
listaSimple = Nodo(10)
listaSimple.siguiente = Nodo(20)
listaSimple.siguiente.siguiente = Nodo(30)

# Imprimir la lista enlazada simple
print("Lista Simple: ", end="")
imprimirListaSimple(listaSimple)

# No es necesario liberar la memoria en Python ya que se maneja automáticamente
