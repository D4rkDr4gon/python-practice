def raiz_cuadrada(x):
    tolerancia = 0.0001  # Tolerancia para considerar la respuesta como válida
    estimado = x / 2.0   # Estimado inicial

    while abs(estimado * estimado - x) > tolerancia:
        # Aplicar fórmula de Newton-Raphson
        estimado = (estimado + x / estimado) / 2.0

    return estimado  # Devolver el estimado final


x = float(input("Ingrese un número: "))
resultado = raiz_cuadrada(x)
print("La raíz cuadrada de", x, "es", resultado)
