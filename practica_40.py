class Jugador:
    def __init__(self, nombre, calidad):
        self.nombre = nombre
        self.calidad = calidad

def pedir_equipo(numero_equipo):
    equipo = []
    print(f"Ingrese los jugadores del Equipo {numero_equipo}:")
    for i in range(5):
        nombre = input(f"Nombre del Jugador {i + 1}: ")
        calidad = int(input(f"Calidad del Jugador {i + 1}: "))
        jugador = Jugador(nombre, calidad)
        equipo.append(jugador)
    return equipo

def calcular_goles(equipo1, equipo2):
    goles_equipo1 = 0
    goles_equipo2 = 0

    # Calcular calidad total de cada equipo
    calidad_equipo1 = sum(jugador.calidad for jugador in equipo1)
    calidad_equipo2 = sum(jugador.calidad for jugador in equipo2)

    # Calcular el mejor jugador de cada equipo
    mejor_jugador_equipo1 = max(equipo1, key=lambda jugador: jugador.calidad)
    mejor_jugador_equipo2 = max(equipo2, key=lambda jugador: jugador.calidad)

    # Calcular el peor jugador de cada equipo
    peor_jugador_equipo1 = min(equipo1, key=lambda jugador: jugador.calidad)
    peor_jugador_equipo2 = min(equipo2, key=lambda jugador: jugador.calidad)

    if calidad_equipo1 > calidad_equipo2:
        goles_equipo1 += 2
    elif calidad_equipo1 < calidad_equipo2:
        goles_equipo2 += 2

    if mejor_jugador_equipo1.calidad > mejor_jugador_equipo2.calidad:
        goles_equipo1 += 1
    elif mejor_jugador_equipo1.calidad < mejor_jugador_equipo2.calidad:
        goles_equipo2 += 1

    if calidad_equipo1 > calidad_equipo2:
        for jugador1, jugador2 in zip(equipo1, equipo2):
            if jugador1.calidad > jugador2.calidad:
                goles_equipo1 += 1
            elif jugador1.calidad < jugador2.calidad:
                goles_equipo2 += 1

    if goles_equipo1 > 0 and peor_jugador_equipo1.calidad < peor_jugador_equipo2.calidad:
        goles_equipo1 -= 1

    if goles_equipo2 > 0 and peor_jugador_equipo2.calidad < peor_jugador_equipo1.calidad:
        goles_equipo2 -= 1

    return goles_equipo1, goles_equipo2

def mostrar_resultados(goles_equipo1, goles_equipo2):
    print("Resultado del partido:")
    print(f"Equipo 1: {goles_equipo1} goles")
    print(f"Equipo 2: {goles_equipo2} goles")

if __name__ == "__main__":
    equipo1 = pedir_equipo(1)
    equipo2 = pedir_equipo(2)

    goles_equipo1, goles_equipo2 = calcular_goles(equipo1, equipo2)
    mostrar_resultados(goles_equipo1, goles_equipo2)
