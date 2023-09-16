class Alumno:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Creación de un objeto Alumno
juan = Alumno("Juan", 20)

# Creación de un puntero a ese objeto (en Python, las variables son referencias)
puntero_juan = juan

# Imprimimos la dirección de memoria (id) y los valores almacenados en el objeto Alumno
print("Dirección de memoria del objeto Alumno 'juan':", id(puntero_juan))
print("Nombre del Alumno:", puntero_juan.nombre)
print("Edad del Alumno:", puntero_juan.edad, "años")

# No es necesario liberar la memoria en Python, el recolector de basura se encargará de esto automáticamente
