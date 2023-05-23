# función que imprime la matriz
def printMatrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

# dimensiones de la matriz
ROWS = 3
COLS = 4

# matriz definida
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

print("Matrix elements:")
printMatrix(matrix)
