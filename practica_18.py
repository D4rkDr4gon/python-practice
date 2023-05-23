class CuentaBancaria:
    def __init__(self, numero, nombre, saldo):
        self.numeroCuenta = numero
        self.nombreTitular = nombre
        self.saldoActual = saldo

    def depositar(self, cantidad):
        self.saldoActual += cantidad

    def retirar(self, cantidad):
        if cantidad > self.saldoActual:
            print("No tienes suficiente saldo para realizar esta transacción.")
        else:
            self.saldoActual -= cantidad

    def mostrarSaldo(self):
        print("Tu saldo actual es: $", self.saldoActual)


def interactuar_con_cuenta_bancaria():
    # Obtener datos del usuario
    print("Bienvenido al banco Python!!! Por favor sigue los pasos para crear tu cuenta y trabajar con ella")
    nombre = input("Nombre del propietario: ")
    numero_cuenta = int(input("Número de cuenta: "))
    saldo = 0.0

    # Crear una nueva cuenta bancaria con número de cuenta, titular y saldo inicial
    cuenta = CuentaBancaria(numero_cuenta, nombre, saldo)

    print("Buenos días,", nombre)

    while True:
        # Preguntar qué acción realizar
        print("¿Qué quieres realizar?")
        print("Depósito: d")
        print("Retiro: r")
        print("Mostrar saldo: m")
        print("Salir: s")
        pregunta = input()

        if pregunta == "d" or pregunta == "D":
            cant_deposito = float(input("Cantidad a depositar: "))
            cuenta.depositar(cant_deposito)
        elif pregunta == "r" or pregunta == "R":
            cant_retirar = float(input("Cantidad a retirar: "))
            cuenta.retirar(cant_retirar)
        elif pregunta == "m" or pregunta == "M":
            cuenta.mostrarSaldo()
        elif pregunta == "s" or pregunta == "S":
            break


interactuar_con_cuenta_bancaria()
