def conversion_opciones():
    option = int(input("Seleccione la opción de conversión:\n"
                       "1. Millas a Kilómetros\n"
                       "2. Pies a Metros\n"
                       "3. Fahrenheit a Celsius\n"))

    if option == 1:
        input_value = float(input("Ingrese la cantidad de millas a convertir: "))
        result = input_value * 1.60934
        print(f"{input_value} millas son equivalentes a {result:.2f} kilómetros.")
    elif option == 2:
        input_value = float(input("Ingrese la cantidad de pies a convertir: "))
        result = input_value * 0.3048
        print(f"{input_value} pies son equivalentes a {result:.2f} metros.")
    elif option == 3:
        input_value = float(input("Ingrese la cantidad de grados Fahrenheit a convertir: "))
        result = (input_value - 32) * 5 / 9
        print(f"{input_value} grados Fahrenheit son equivalentes a {result:.2f} grados Celsius.")
    else:
        print("Opción inválida.")

conversion_opciones()
