class Alumno:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Creación de una instancia de la clase Alumno (equivalente al new en C++)
alumno_dinamico = Alumno("Juan", 20)

# Imprimir los valores del Alumno dinámico
print("Nombre del Alumno:", alumno_dinamico.nombre)
print("Edad del Alumno:", alumno_dinamico.edad, "años")

# No es necesario liberar la memoria en Python, el recolector de basura se encargará de esto automáticamente
