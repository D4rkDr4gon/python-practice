# funciones: bloques de código que se pueden reutilizar y realizan actividades específicas
def Suma(a, b):
    Var = a + b
    return Var

def Resta(a, b):
    Var = a - b
    return Var

def Multiplicar(a, b):
    Var = a * b
    return Var

def Dividir(a, b):
    Var = a / b
    return Var

# variables
a = 0.0
b = 0.0
Resultado = 0.0
i = 0

# datos al usuario
a = float(input("Ingresa un valor: "))
b = float(input("Ingresa otro valor: "))

print("Tipo de operación a realizar:")
print("1 = suma")
print("2 = resta")
print("3 = multiplicación")
print("4 = división")
i = int(input())

# switch
if i == 1:
    Resultado = Suma(a, b)
    print("resultado =", Resultado)
elif i == 2:
    Resultado = Resta(a, b)
    print("resultado =", Resultado)
elif i == 3:
    Resultado = Multiplicar(a, b)
    print("resultado =", Resultado)
elif i == 4:
    Resultado = Dividir(a, b)
    print("resultado =", Resultado)
else:
    print("No es válido")
