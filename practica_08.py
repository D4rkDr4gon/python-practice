# clase
class Alumno:
    def __init__(self, nombre, legajo):
        self.nombre = nombre
        self.legajo = legajo

# variables
un_alumno = Alumno("", "")

print("Ingrese nombre: ")
un_alumno.nombre = input()

print("Ingrese legajo: ")
un_alumno.legajo = input()

if un_alumno.nombre == "lucciano" and un_alumno.legajo == "214.555-3":
    print("¡Bienvenido!", un_alumno.nombre)
elif un_alumno.nombre == "admin" and un_alumno.legajo == "0000":
    print("Permiso de administrador autorizado. ¡Bienvenido!")
else:
    print("No tiene acceso")
