def stop_criterion(x0, x1):
    return abs((x0 - x1) / (1 - ((x0 - x1) / (x1 - x0))))

def root(a, x0):
    x1 = 0.5 * (x0 + a/x0)
    while stop_criterion(x1, x0) >= 0.01: 
        x0, x1 = x1, (0.5 * (x1 + a/x1))
    return x1


print(root(16, 10)) # -> 4.000000000013422
# print(root(256, 5, 10**(-5)))  # -> 16.0
# print(root(49, 16, 10**(-5)))  # -> 7.000000000001278
# print(root(25, 30, 10**(-5)))  # -> 5.0
