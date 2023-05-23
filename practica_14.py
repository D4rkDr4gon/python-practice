# Enumeración
class DiasSemana:
    Lunes = 1
    Martes = 2
    Miercoles = 3
    Jueves = 4
    Viernes = 5
    Sabado = 6
    Domingo = 7

def main():
    dia = int(input("¿Qué día de la semana es hoy? (1=Lunes, 2=Martes, etc.): "))

    # Switch
    if dia == DiasSemana.Lunes:
        print("Hoy es lunes.")
    elif dia == DiasSemana.Martes:
        print("Hoy es martes.")
    elif dia == DiasSemana.Miercoles:
        print("Hoy es miércoles.")
    elif dia == DiasSemana.Jueves:
        print("Hoy es jueves.")
    elif dia == DiasSemana.Viernes:
        print("Hoy es viernes.")
    elif dia == DiasSemana.Sabado:
        print("Hoy es sábado.")
    elif dia == DiasSemana.Domingo:
        print("Hoy es domingo.")
    else:
        print("Día inválido.")

if __name__ == "__main__":
    main()
