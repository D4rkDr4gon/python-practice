maximo = 0
print("Ingrese 10 números:")

# bucle for
for i in range(10):
    numero = 0
    
    if i == 0:
        print("Ingrese el primer número:")
        maximo = int(input())
    else:
        print("Ingrese el siguiente:")
        numero = int(input())
        
        if numero > maximo:
            maximo = numero

print("El mayor es:", maximo)
