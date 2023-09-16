class Producto:
    def __init__(self):
        self.NomProduct = ""
        self.codigo = 0
        self.marca = ""
        self.precio = 0

def InsertarProducto(producto, SIZE):
    for i in range(SIZE):
        # Insertar datos
        producto[i].NomProduct = input("nombre del producto: ")
        producto[i].marca = input("marca: ")
        producto[i].precio = int(input("precio: "))

        # Organizar código
        if producto[i].NomProduct.lower() == "martillo":
            producto[i].codigo = 100
        elif producto[i].NomProduct.lower() == "destornillador":
            producto[i].codigo = 200
        else:
            # Si no se reconoce el nombre del producto, asignar un código por defecto
            producto[i].codigo = 0

def OrdenarLista(array):
    array.sort(key=lambda x: (x.codigo, x.NomProduct))

def BuscarProducto(array, nombre, marca):
    for i, producto in enumerate(array):
        if producto.NomProduct == nombre and producto.marca == marca:
            return i  # Se encontró el producto, devolver su índice
    return -1  # No se encontró el producto

if __name__ == "__main__":
    SIZE = 4
    lista = [Producto() for _ in range(SIZE)]
    nombre = input("nombre del producto a buscar: ").lower()
    marca = input("marca del producto a buscar: ").lower()

    # Insertar productos
    InsertarProducto(lista, SIZE)

    # Ordenar productos
    OrdenarLista(lista)

    print("-------------------------")

    # Buscar productos
    indice = BuscarProducto(lista, nombre, marca)

    if indice != -1:
        print(f"El producto se encuentra en la posición {indice}")
    else:
        print("El producto no fue encontrado")

    print("-------------------------")

    # Imprimir lista de productos
    for i, producto in enumerate(lista):
        print(f"Producto {i + 1}:")
        print("Nombre:", producto.NomProduct)
        print("Marca:", producto.marca)
        print("Precio:", producto.precio)
        print("Código:", producto.codigo)
        print()
