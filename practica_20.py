import struct

def dec_pfsp():
    decimal_value = float(input("Ingrese un número decimal: "))

    sign = 0 if decimal_value >= 0 else 1
    decimal_value = abs(decimal_value)
    exponent = 0
    fraction = decimal_value

    if fraction >= 2.0:
        while fraction >= 2.0:
            fraction /= 2.0
            exponent += 1
    elif fraction < 1.0:
        while fraction < 1.0:
            fraction *= 2.0
            exponent -= 1

    fraction -= 1.0
    exponent += 127

    float_bits = sign << 31 | exponent << 23
    for i in range(23):
        fraction *= 2.0
        float_bits |= int(fraction) << (22 - i)
        fraction -= int(fraction)

    print("El equivalente en punto flotante es:", struct.unpack('f', struct.pack('I', float_bits))[0])


def char_ascii():
    c = input("Ingrese un caracter: ")
    print("El equivalente en código ASCII de '", c, "' es", ord(c))


def bin_ascii():
    binary_str = input("Ingrese un número binario: ")
    ascii_char = chr(int(binary_str, 2))
    print("El equivalente en ASCII es:", ascii_char)


def ascii_bin():
    ascii_code = int(input("Ingrese un código ASCII: "))
    binary = bin(ascii_code)[2:].zfill(8)
    print("El equivalente en binario es:", binary)


def bin_hex():
    binary_str = input("Ingrese un número binario: ")
    hex_value = hex(int(binary_str, 2))[2:]
    print("El equivalente en hexadecimal es:", hex_value)


def bin_dec():
    binary_str = input("Ingrese un número binario: ")
    decimal_value = int(binary_str, 2)
    print("El equivalente en decimal es:", decimal_value)


def pfsp_bin():
    float_value = float(input("Ingrese un número de punto flotante en formato IEEE 754 (32 bits): "))
    float_bits = struct.unpack('I', struct.pack('f', float_value))[0]
    binary = bin(float_bits)[2:].zfill(32)
    print("El equivalente en binario es:", binary)


def hex_dec():
    hex_value = input("Ingrese un número hexadecimal: ")
    dec_value = int(hex_value, 16)
    print("El equivalente en decimal es:", dec_value)


while True:
    print("Conversor de unidades!")
    print("1 = Caracteres a ASCII")
    print("2 = ASCII a binario")
    print("3 = Binario a hexadecimal")
    print("4 = Binario a decimal")
    print("5 = Binario a ASCII")
    print("6 = Decimal a Punto Flotante Simple Precisión")
    print("7 = Punto Flotante Simple Precisión a binario")
    print("8 = Hexadecimal a Decimal")
    print("9 = Fin del programa")
    
    eleccion = int(input("Ingrese su elección: "))

    if eleccion == 1:
        char_ascii()
    elif eleccion == 2:
        ascii_bin()
    elif eleccion == 3:
        bin_hex()
    elif eleccion == 4:
        bin_dec()
    elif eleccion == 5:
        bin_ascii()
    elif eleccion == 6:
        dec_pfsp()
    elif eleccion == 7:
        pfsp_bin()
    elif eleccion == 8:
        hex_dec()
    elif eleccion == 9:
        break
    else:
        print("Opción inválida")

print("Fin del programa")
