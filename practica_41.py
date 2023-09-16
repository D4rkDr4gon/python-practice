class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

class Factura:
    def __init__(self, numero, fecha, monto):
        self.numero = numero
        self.fecha = fecha
        self.monto = monto

def insertar_factura(facturas, numero):
    print(f"Ingrese los datos de la factura #{numero}:")
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    año = int(input("Año: "))
    monto = float(input("Monto: "))

    fecha = Fecha(dia, mes, año)
    factura = Factura(numero, fecha, monto)
    facturas.append(factura)

def buscar_factura(facturas, numero):
    for factura in facturas:
        if factura.numero == numero:
            return factura
    return None

def main():
    facturas = []

    print("Bienvenido al sistema de facturación")

    for i in range(1, 11):
        insertar_factura(facturas, i)

    numero_buscar = int(input("Ingrese el número de factura a buscar: "))
    factura_encontrada = buscar_factura(facturas, numero_buscar)

    if factura_encontrada:
        print("Factura encontrada:")
        print(f"Número de factura: {factura_encontrada.numero}")
        print(f"Fecha: {factura_encontrada.fecha.dia}/{factura_encontrada.fecha.mes}/{factura_encontrada.fecha.año}")
        print(f"Monto: {factura_encontrada.monto}")
    else:
        print("La factura no fue encontrada.")

if __name__ == "__main__":
    main()
