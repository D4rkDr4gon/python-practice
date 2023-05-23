CantAsig = int(input("cantidad de asignaturas: "))

Asig = []
Sum = 0

for i in range(CantAsig):
    nota = float(input("nota asignatura {}: ".format(i)))
    Asig.append(nota)
    Sum += nota

promedio = Sum / CantAsig
print("tu promedio es:", promedio)
