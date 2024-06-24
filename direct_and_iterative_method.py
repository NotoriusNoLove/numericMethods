import numpy as np

# Вспомогательные функции для метода прямой итерации

def newton_stop_criterion(x_next, x_current):
    numerator = x_next - x_current
    denominator = 1 - ((x_next - x_current) / (x_current - x_next))
    return abs(numerator / denominator)

def newton_derivative(arr):
    return arr[1:] * np.arange(1, len(arr))

def newton_function(x, arr):
    result = 0
    for i in range(1, len(arr) + 1):
        result += x**i * arr[i - 1]
    return result

def newton_method(f, arr, x_initial, tolerance=1e-2, factor=1):
    x1 = x_initial - newton_function(x_initial, arr) / newton_function(x_initial, newton_derivative(arr))
    x_values = [x_initial, x1]

    while newton_stop_criterion(x_values[1], x_values[0]) >= tolerance:
        temp = x_values[1]
        x_values[1] = x_values[1] - factor * newton_function(x_values[1], arr) / newton_function(x_values[1], newton_derivative(arr))
        x_values[0] = temp

    return x_values[1]

# Метод прямой итерации

def generate_polynomial(A):
    if len(A) == 2:
        return [A[0][0]*A[1][1] - A[0][1]*A[1][0], -(A[1][1]+A[0][0]), 1]
    elif len(A) == 3:
        return [A[0][0]*A[1][1]*A[2][2] + A[0][1]*A[1][2]*A[2][0] + A[0][2]*A[1][0]*A[2][1]
                - A[0][2]*A[1][1]*A[2][0] - A[0][1]*A[1][0]*A[2][2] - A[0][0]*A[1][2]*A[2][1],
                A[0][0]*A[1][1] - A[0][0]*A[2][2] - A[1][1]*A[2][2] + A[0][2]*A[2][0]
                + A[0][1]*A[1][0] + A[1][2]*A[2][1],
                A[0][0] + A[1][1] + A[2][2],
                1]
    return []

matrix1 = np.array([[2, 2, 3], [4, 5, 6], [7, 8, 9]]) # -> 0.11596922694376219
polynomial = generate_polynomial(matrix1)

print(newton_method(newton_function, polynomial, 1))

# Вспомогательные функции для метода итераций

def iteration_stop_criterion(x_new, x_old, tolerance=1e-3):
    return np.abs(x_new - x_old) < tolerance

# Метод итераций

def iteration_method(A, tolerance=1e-3):
    x_old = np.ones(len(A))
    x_new = np.dot(A, x_old)

    eigenvalue_old = x_new[0] / x_old[0]
    eigenvalue_new = eigenvalue_old

    iteration_count = 0

    while True:
        iteration_count += 1

        x_old = x_new.copy()
        x_new = np.dot(A, x_old)

        eigenvalue_old = eigenvalue_new
        eigenvalue_new = x_new[0] / x_old[0]

        # Нормализация вектора каждые 5 итераций    
        if iteration_count % 5 == 0:
            x_new /= np.linalg.norm(x_new)

        if iteration_stop_criterion(eigenvalue_new, eigenvalue_old, tolerance):
            break

    # Нормализация вектора в конце
    x_new /= np.linalg.norm(x_new)

    return x_new, eigenvalue_new

matrix2 = np.array([[5, 1, 2], [1, 4, 1], [2, 1, 3]])

eigen_vector, eigen_value = iteration_method(matrix2)

print("Собственный вектор для матрицы matrix2:", eigen_vector) # -> [0.75249496 0.4318604  0.49724031]
print("Собственное значение для матрицы matrix2:", eigen_value) # -> 6.8958704371104655
