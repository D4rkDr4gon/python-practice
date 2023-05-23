decimal = int(input("Ingrese un número decimal: "))
binario = 0
exp = 0

while decimal != 0:
    digito = decimal % 2
    binario += digito * 10 ** exp
    exp += 1
    decimal //= 2

print("El número en binario es:", binario)
