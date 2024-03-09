def deriv(arr):
    return [arr[i]*i for i in range(1, len(arr))]

def stop(x0, x1):
    return abs((x0 - x1) / (1 - ((x0 - x1) / (x1 - x0))))

def f(x, arr):
    return sum([(x**i * arr[i - 1]) for i in range(1, len(arr) + 1)])

def help(x, arr, c=1):
    return x - c*f(x, arr) / f(x, deriv(arr)) 
# ------------------

arr = [-6, 11, -6, 1] 
x0 = 10

# --------------
def newton(f, x0, c = 1, eps = 1e-5):
    x1 = help(x0, arr)

    while stop(x1, x0) >= eps: 
        x0, x1 = x1, help(x1, arr, c)
    return x1

def newton_simple(f, x0, eps = 1e-5):
    x = [x0, help(x0, arr)] 

    while stop(x[1], x[0]) >= eps: 
        x[0], x[1] = x[1] , x[1] - f(x[1], arr) / f(x0, deriv(arr)) 
    return x[1]

def secant(f, x0, eps = 1e-5):
    x1 = x0 - f(x0, arr) / f(x0, deriv(arr))
    x = [x0, x1]
    
    while stop(x[1], x[0]) > eps:
        x[0], x[1] = x[1], x[0] - (f(x[0], arr) * (x[1] - x[0])) / (f(x[1], arr) - f(x[0], arr))
    return x[1]


print(newton(f, x0))       

print(newton(f, x0, 3))  #broiden

print(newton_simple(f, x0)) 

print(secant(f, x0))