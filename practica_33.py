def convertirCelsiusToFahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def convertirFahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def mostrarResultado(valor, unidadOrigen, unidadDestino):
    print(valor, unidadOrigen, "equivale a", convertirCelsiusToFahrenheit(valor), unidadDestino)

temperatura = {}
print("Conversor de Temperaturas")
temperatura["valor"] = float(input("Ingrese un valor de temperatura: "))
temperatura["unidad"] = input("Ingrese la unidad de temperatura (C o F): ")
if temperatura["unidad"] == "C":
    mostrarResultado(temperatura["valor"], "Celsius", "Fahrenheit")
elif temperatura["unidad"] == "F":
    mostrarResultado(temperatura["valor"], "Fahrenheit", "Celsius")
else:
    print("Unidad de temperatura no válida. Por favor, ingrese 'C' o 'F'.")
