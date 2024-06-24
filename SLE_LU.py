import numpy as np


def matrix_preparation(mat):
    A_matrix = mat[:, :-1]
    b_vector = mat[:, -1].reshape(-1, 1)
    return A_matrix, b_vector


def decompose_LU(mat, vec):
    n = len(mat)
    lu_decomp = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            temp_sum = 0
            for k in range(i):
                temp_sum += lu_decomp[i, k] * lu_decomp[k, j]
            lu_decomp[i, j] = mat[i, j] - temp_sum
        for j in range(i + 1, n):
            temp_sum = 0
            for k in range(i):
                temp_sum += lu_decomp[j, k] * lu_decomp[k, i]
            lu_decomp[j, i] = (mat[j, i] - temp_sum) / lu_decomp[i, i]

    y_vector = np.zeros(n)
    for i in range(n):
        temp_sum = 0
        for k in range(i):
            temp_sum += lu_decomp[i, k] * y_vector[k]
        y_vector[i] = vec[i] - temp_sum

    x_vector = np.zeros(n)
    for i in range(n - 1, -1, -1):
        temp_sum = 0
        for k in range(i + 1, n):
            temp_sum += lu_decomp[i, k] * x_vector[k]
        x_vector[i] = (y_vector[i] - temp_sum) / lu_decomp[i, i]

    return x_vector


matrix_1, vector_1 = matrix_preparation(np.array([
    [5, 0, 1, 11],
    [2, 6, -2, 8],
    [-3, 2, 10, 6]
], dtype='float64'))

matrix_2, vector_2 = matrix_preparation(np.array([
    [2, 1, 4, 16],
    [3, 2, 1, 10],
    [1, 3, 3, 16],
], dtype='float64'))

matrix_3, vector_3 = matrix_preparation(np.array([
    [-3, 2.099, 6, 3.901],
    [10, -7, 0, 7],
    [5, -1, 5, -6]
], dtype='float64'))

print(" ".join(map(str, decompose_LU(matrix_1, vector_1))))  # -> 2.0 1.0 1.0
print(" ".join(map(str, decompose_LU(matrix_2, vector_2))))  # -> 1.0 2.0 3.0
# -> -3.3588803732091357 -5.798400533155909 0.9992002665778078
print(" ".join(map(str, decompose_LU(matrix_3, vector_3))))
