# Definición de la clase Nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Clase para implementar una pila
class Pila:
    def __init__(self):
        self.cima = None

    # Método para apilar un elemento en la pila
    def push(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo

    # Método para desapilar y obtener el elemento en la cima de la pila
    def pop(self):
        if self.isEmpty():
            print("La pila está vacía.")
            return None  # Valor de error
        valor = self.cima.valor
        self.cima = self.cima.siguiente
        return valor

    # Método para verificar si la pila está vacía
    def isEmpty(self):
        return self.cima is None

# Función para mostrar los elementos de la pila
def mostrar_pila(pila):
    print("Elementos en la pila:")
    while not pila.isEmpty():
        valor = pila.pop()
        print(valor, end=" ")
    print()

# Crear una instancia de la clase Pila
pila = Pila()

# Apilar elementos en la pila
pila.push(10)
pila.push(20)
pila.push(30)

# Mostrar y desapilar elementos de la pila
mostrar_pila(pila)
