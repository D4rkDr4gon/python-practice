def mostrar_arr(array):
    for i, element in enumerate(array):
        print(i, ",", element)

def orden_simple(array):
    size = len(array)
    ord = 0

    for i in range(size - 1):
        ord = 1

        for j in range(size - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                ord = 0

                mostrar_arr(array)
                print("------------------")

        if ord == 1:
            break

def busqueda_lineal(array, valor):
    size = len(array)
    encontrado = False

    for i in range(size):
        if array[i] == valor:
            print("La posición:", i, "El valor:", array[i])
            encontrado = True

    if not encontrado:
        print("Valor no encontrado")

def busqueda_binaria(array, valor):
    inicio = 0
    fin = len(array) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if array[medio] == valor:
            return medio + 1
        elif array[medio] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1

        print("Estoy evaluando entre la posición", inicio, "y la posición", fin)

    return -1

def insertar_ord(array, elemento):
    size = len(array)
    i = size - 1

    while i >= 0 and array[i] > elemento:
        array[i + 1] = array[i]
        i -= 1

    array[i + 1] = elemento

# main
array = [0] * 10

for i in range(10):
    elemento = int(input())
    insertar_ord(array, elemento)

mostrar_arr(array)
