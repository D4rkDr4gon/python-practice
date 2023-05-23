# Fibonacci
num1 = 0
num2 = 1
i = 1

# bucle while
while i <= 10:
    print(num1, end=", ")
    sum = num1 + num2
    num1 = num2
    num2 = sum
    i += 1
