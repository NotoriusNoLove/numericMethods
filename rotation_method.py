import numpy as np
import math


def stop_criterion(element, eps=1e-3):
    return abs(element) < eps


def get_max_abs_element(matrix):
    max_element = None

    for i in range(matrix.shape[0]):
        for j in range(i + 1, matrix.shape[1]):
            if max_element is None or abs(matrix[i][j]) > abs(max_element):
                max_element = matrix[i][j]

    return max_element


def get_rotation_matrix(size, i, j, phi):
    sin_phi = math.sin(phi)
    cos_phi = math.cos(phi)

    matrix_H = np.eye(size)
    matrix_H[i, i] = cos_phi
    matrix_H[j, j] = cos_phi
    matrix_H[i, j] = -sin_phi
    matrix_H[j, i] = sin_phi

    return matrix_H


def rotation_method(matrix_A, eps=1e-3):
    n = matrix_A.shape[0]
    eigen_vectors = np.eye(n)

    while not stop_criterion(get_max_abs_element(matrix_A), eps):
        max_element = get_max_abs_element(matrix_A)

        # Найти индексы i и j для максимального элемента вне диагонали
        for i in range(n):
            for j in range(i + 1, n):
                if matrix_A[i, j] == max_element:
                    break
            if matrix_A[i, j] == max_element:
                break

        # Вычисление угла phi
        if matrix_A[i, i] == matrix_A[j, j]:
            phi = math.pi / 4
        else:
            phi = 0.5 * \
                math.atan2(2 * matrix_A[i, j], matrix_A[i, i] - matrix_A[j, j])

        # Построение матрицы вращения
        matrix_H = get_rotation_matrix(n, i, j, phi)

        # Применение вращения к матрице A и накопление вращений для собственных векторов
        matrix_A = matrix_H.T @ matrix_A @ matrix_H
        eigen_vectors = eigen_vectors @ matrix_H

    eigen_values = np.diag(matrix_A)

    return eigen_values, eigen_vectors


# Тест 1
matrix_A_1 = np.array([
    [2, 1],
    [1, 3]
], dtype='float64')

eigen_values_A_1, eigen_vectors_A_1 = rotation_method(matrix_A_1)

# -> [1.38196601 3.61803399]
print('Eigen values of matrix A_1:', eigen_values_A_1)
# -> [[ 0.85065081 -0.52573111] [0.52573111 0.85065081]]
print('Eigen vectors of matrix A_1:', eigen_vectors_A_1)
