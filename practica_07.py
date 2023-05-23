n = int(input("Ingrese un número: "))
m = int(input("Ingrese el número de multiplicación: "))

for i in range(m, m * n + 1, m):
    print(i, end=" ")

print()
