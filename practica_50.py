class Cliente:
    def __init__(self, DNI, nombre):
        self.DNI = DNI
        self.nombre = nombre

class TreeNode:
    def __init__(self, cliente):
        self.cliente = cliente
        self.left = None
        self.right = None

# Función para crear un nuevo nodo con el valor dado
def crearNodo(valor):
    nuevoNodo = TreeNode(valor)
    return nuevoNodo

# Función para insertar un nuevo elemento en el árbol binario de búsqueda
def insertar(root, valor):
    if root is None:
        return crearNodo(valor) # Si el nodo es nulo, crea un nuevo nodo con el valor dado
    # Si el valor es menor que el valor actual, inserta en el subárbol izquierdo
    if valor.DNI < root.cliente.DNI:
        root.left = insertar(root.left, valor)
    # Si el valor es mayor que el valor actual, inserta en el subárbol derecho
    elif valor.DNI > root.cliente.DNI:
        root.right = insertar(root.right, valor)
    return root # Retorna el nodo raíz actual después de la inserción

# Recorrido en inorden de manera recursiva
def inordenRecursivo(root):
    if root is None:
        return
    inordenRecursivo(root.left)
    print("DNI: " + str(root.cliente.DNI) + " Nombre: " + root.cliente.nombre)
    inordenRecursivo(root.right)

# Función para buscar un cliente por su DNI en el árbol
def buscarPorDNI(root, dni):
    if root is None or root.cliente.DNI == dni:
        return root
    if dni < root.cliente.DNI:
        return buscarPorDNI(root.left, dni)
    return buscarPorDNI(root.right, dni)

# Función para encontrar el nodo con el valor mínimo en un subárbol
def encontrarMinimo(root):
    actual = root
    while actual.left is not None:
        actual = actual.left
    return actual

# Función para eliminar un cliente por su DNI del árbol
def eliminarPorDNI(root, dni):
    if root is None:
        return root
    if dni < root.cliente.DNI:
        root.left = eliminarPorDNI(root.left, dni)
    elif dni > root.cliente.DNI:
        root.right = eliminarPorDNI(root.right, dni)
    else:
        # Nodo con un solo hijo o sin hijos
        if root.left is None:
            temp = root.right
            del root
            return temp
        elif root.right is None:
            temp = root.left
            del root
            return temp
        # Nodo con dos hijos, encontrar el sucesor inorden (nodo más pequeño en el subárbol derecho)
        temp = encontrarMinimo(root.right)
        # Copiar el contenido del sucesor inorden a este nodo
        root.cliente = temp.cliente
        # Eliminar el sucesor inorden
        root.right = eliminarPorDNI(root.right, temp.cliente.DNI)
    return root

root = None # Inicializa el árbol binario de búsqueda como vacío

while True:
    opcion = int(input("1. Insertar cliente\n2. Verificar si el arbol esta balanceado\n3. Imprimir arbol\n4. Buscar cliente por DNI\n5. Eliminar cliente por DNI\n6. Salir\nIngrese una opcion: "))

    if opcion == 1:
        dni = int(input("Ingrese el DNI del cliente: "))
        nombre = input("Ingrese el nombre del cliente: ")
        cliente = Cliente(dni, nombre)
        root = insertar(root, cliente)
    elif opcion == 2:
        # Implementa la verificación de balance aquí si lo deseas
        pass
    elif opcion == 3:
        inordenRecursivo(root)
    elif opcion == 5:
        dni = int(input("Ingrese el DNI del cliente que desea eliminar: "))
        root = eliminarPorDNI(root, dni)
    elif opcion == 4:
        dni = int(input("Ingrese el DNI del cliente que desea buscar: "))
        encontrado = buscarPorDNI(root, dni)
        if encontrado is not None:
            print("DNI: " + str(encontrado.cliente.DNI) + " Nombre: " + encontrado.cliente.nombre)
        else:
            print("Cliente no encontrado.")
    elif opcion == 6:
        break
    else:
        print("Opcion invalida")