def calcularBMI(peso, altura):
    return peso / (altura * altura)

def mostrarCategoria(bmi):
    if bmi < 18.5:
        print("Bajo peso")
    elif bmi < 25.0:
        print("Peso normal")
    elif bmi < 30.0:
        print("Sobrepeso")
    else:
        print("Obesidad")

print("Calculadora de BMI")
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
bmi = calcularBMI(peso, altura)
print("Su BMI es:", bmi)
print("Categoría:", end=" ")
mostrarCategoria(bmi)
