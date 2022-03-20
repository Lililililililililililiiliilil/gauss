import numpy as np
import sys


def gauss(matrix, main_x):
    n = len(matrix)
    k = 0

    # прямой ход метода Гаусса

    for row in range(n):
        matrix[row] = matrix[row] * 1 / matrix[row, main_x[k]]
        for row_below in range(row + 1, n):
            matrix[row_below] = matrix[row_below] - matrix[row] * matrix[row_below, main_x[k]]
        k += 1

    k -= 1

    # обратный ход метода Гаусса

    for row in range(n - 1, 0, -1):
        for row_upper in range(row - 1, -1, -1):
            matrix[row_upper] = matrix[row_upper] - matrix[row] * matrix[row_upper, main_atr[k]]
        k -= 1

    return matrix


# вводится размерность матрицы
n, m = map(int, input().split())

d2_array = []

for i in range(n):
    d2_array.append(list(map(int, input().split())))

matrix = np.matrix(d2_array)

main_atr = list(map(int, input().split()))  # вводятся в строчку номера главных переменных
main_atr = list(map(lambda x: x - 1, main_atr))
gauss(matrix, main_atr)

for i in range(n):
    for j in range(m):
        print(matrix[i, j], end=' ')
    print()
