def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = int(input("Ingresa un número: "))
b = int(input("Ingresa un número: "))

mcd = gcd(a, b)
print("El MCD de", a, "y", b, "es", mcd)
