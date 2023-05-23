# clase
class Fraccion:
    def __init__(self, n, d):
        self.numerador = n
        self.denominador = d

    def imprimir(self):
        print(self.numerador, "/", self.denominador)

    def __add__(self, f):
        n = self.numerador * f.denominador + f.numerador * self.denominador
        d = self.denominador * f.denominador
        resultado = Fraccion(n, d)
        return resultado

    def __sub__(self, f):
        n = self.numerador * f.denominador - f.numerador * self.denominador
        d = self.denominador * f.denominador
        resultado = Fraccion(n, d)
        return resultado

    def __mul__(self, f):
        n = self.numerador * f.numerador
        d = self.denominador * f.denominador
        resultado = Fraccion(n, d)
        return resultado

    def __truediv__(self, f):
        n = self.numerador * f.denominador
        d = self.denominador * f.numerador
        resultado = Fraccion(n, d)
        return resultado

# variables
n = int(input("Numerador de la primera fracción: "))
d = int(input("Denominador de la primera fracción: "))
n1 = int(input("Numerador de la segunda fracción: "))
d1 = int(input("Denominador de la segunda fracción: "))

# instancias de la clase Fraccion
f1 = Fraccion(n, d)
f2 = Fraccion(n1, d1)

# operaciones
suma = f1 + f2
resta = f1 - f2
producto = f1 * f2
division = f1 / f2

# imprimir en pantalla
print("La suma de las fracciones es:")
suma.imprimir()

print("La resta de las fracciones es:")
resta.imprimir()

print("El producto de las fracciones es:")
producto.imprimir()

print("La división de las fracciones es:")
division.imprimir()
