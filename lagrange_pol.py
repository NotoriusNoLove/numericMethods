def lagrange_interpolation(x_points, y_points, eval_point):
    n = len(x_points)  # Number of x points

    result = 0  # Initialize the result

    # Calculate the Lagrange basis polynomials and sum them
    for i in range(n):

        term = y_points[i]  # Start with the function value y[i]

        for j in range(n):
            # Skip the same point
            if j != i and x_points[i] != x_points[j]:
                term *= (eval_point - x_points[j]) / \
                    (x_points[i] - x_points[j])

        # Add the evaluated term to the result
        result += term

    return result


# test 1
x_vals_1 = [2, 3, 4, 5]
y_vals_1 = [7, 5, 8, 7]

print(lagrange_interpolation(x_vals_1, y_vals_1, 2.5))  # -> 4.8125

# test 2
x_vals_2 = [-1, 0, 1, 3]
y_vals_2 = [2, 4, 5, 0]

print(lagrange_interpolation(x_vals_2, y_vals_2, 0.5))  # -> 4.6875

# test 3
x_vals_3 = [1, 1.2, 1.4, 1.6, 1.8, 1.2]
y_vals_3 = [0, 0.4, 0.896, 1.5008, 2.22464, 3.075712]

print(lagrange_interpolation(x_vals_3, y_vals_3, 1))   # -> 0.0
