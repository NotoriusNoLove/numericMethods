import numpy as np


def search(row, shift=0):
    return search(row, shift + 1) if row[shift] == 0 else row[shift]


def reverse(aug_matrix):
    result = []
    for i in range(len(aug_matrix)-1, -1, -1):
        for j in range(i+1, len(aug_matrix[i])-1):
            aug_matrix[i][j] *= result[::-1][j-i-1]
        result.append(
            (aug_matrix[i][i:][-1] - sum(aug_matrix[i][i:][1:-1])) / aug_matrix[i][i:][0])
    return result[::-1]


def single_division_method(aug_matrix):
    for i in range(len(aug_matrix)):
        el = search(aug_matrix[i])
        for t in range(len(aug_matrix[i])):
            aug_matrix[i][t] = aug_matrix[i][t] / el
        if len(aug_matrix)-1 == i:
            for k in range(len(aug_matrix) - 1):
                el = search(aug_matrix[i])
                for t in range(len(aug_matrix[i])):
                    aug_matrix[i][t] = aug_matrix[i][t] - \
                        aug_matrix[k][t] * el
        else:
            el = search(aug_matrix[i+1])
            for t in range(len(aug_matrix[i + 1])):
                aug_matrix[i + 1][t] -= aug_matrix[i][t] * el
    return aug_matrix


def rectangle_method(aug_matrix):
    for i in range(len(aug_matrix) - 1):
        aug_matrix[i, :] = aug_matrix[i, :]/aug_matrix[i, i]
        for j in range(i + 1, len(aug_matrix)):
            for k in range(i + 1, len(aug_matrix) + 1):
                aug_matrix[j, k] -= aug_matrix[i, k]*aug_matrix[j, i]
            aug_matrix[j, i] = 0
    aug_matrix[-1, :] = aug_matrix[-1, :]/aug_matrix[-1, -2]
    return aug_matrix


test_1 = np.array([[5, 0, 1, 11],
                   [2, 6, -2, 8],
                   [-3, 2, 10, 6]],
                  dtype='float64')
test_2 = np.array([[2, 1, 4, 16],
                   [3, 2, 1, 10],
                   [1, 3, 3, 16]],
                  dtype='float64')

print('single_division_method')

for i in range(len(tmp := reverse(single_division_method(test_1)))):
    print(f"X{i+1} = {tmp[i]:.5f}")
print('rectangle_method')

for i in range(len(tmp := reverse(rectangle_method(test_2)))):
    print(f"X{i+1} = {tmp[i]:.5f}")
