import math
import numpy as np

# Исходные данные
x_points = [2, 3, 4, 5]
f_points = [7, 5, 8, 7]


def solve_linear_equations(matrix):
    A = matrix[:, :-1]
    b = matrix[:, -1].reshape(-1, 1)
    return np.linalg.solve(A, b).tolist()


def least_squares_fit(x_points, f_points, polynomial_degree, solver=solve_linear_equations):
    matrix = []

    s_0 = len(x_points)
    s_terms = [s_0]

    t_0 = sum(f_points)
    t_terms = [t_0]

    for i in range(1, 2 * polynomial_degree + 1):
        x_powers = [x**i for x in x_points]
        s_terms.append(sum(x_powers))

        if i <= math.ceil((polynomial_degree + 1) / 2) + 1:
            xf_products = [x * f for x, f in zip(x_powers, f_points)]
            t_terms.append(sum(xf_products))

    for i in range(polynomial_degree + 1):
        matrix.append([*s_terms[i:i+polynomial_degree+1], t_terms[i]])

    matrix = np.array(matrix, dtype='float64')

    return solver(matrix)


# Тесты
# -> [[5.700000000000004], [0.2999999999999991]]
print(least_squares_fit(x_points, f_points, 1))
# -> [[8.449999999999905], [-1.4499999999999404], [0.24999999999999156]]
print(least_squares_fit(x_points, f_points, 2))
