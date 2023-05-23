n = int(input("Ingrese un número entero positivo: "))

es_primo = True

if n < 2:
    es_primo = False
else:
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            es_primo = False
            break

if es_primo:
    print(n, "es un número primo")
else:
    print(n, "no es un número primo")
