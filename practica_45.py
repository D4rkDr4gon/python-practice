# Definición de la clase Nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Clase para implementar una cola
class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    # Método para encolar un elemento en la cola
    def encolar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.final is None:
            self.frente = self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

    # Método para desencolar y obtener el elemento del frente de la cola
    def desencolar(self):
        if self.frente is None:
            print("La cola está vacía.")
            return None  # Valor de error
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None  # Si se elimina el último elemento, actualizar 'final'
        return valor

    # Método para verificar si la cola está vacía
    def isEmpty(self):
        return self.frente is None

# Función para mostrar los elementos de la cola
def mostrar_cola(cola):
    print("Elementos en la cola:")
    while not cola.isEmpty():
        valor = cola.desencolar()
        print(valor, end=" ")
    print()

# Crear una instancia de la clase Cola
cola = Cola()

# Encolar elementos
cola.encolar(10)
cola.encolar(20)
cola.encolar(30)

# Mostrar y desencolar elementos de la cola
mostrar_cola(cola)
