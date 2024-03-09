def newF(arr, x):
    return sum(arr[i]*(x**i) for i in range(len(arr)))

def deriv(arr):
    return [arr[i]*i for i in range(1, len(arr))]

def first(arr, a, x):
    return a - (newF(arr, a)/(newF(arr, x) - newF(arr, a)))*(x-a)

def second(arr, b, x):
    return x - (newF(arr, x)/(newF(arr, b) - newF(arr, x)))*(b-x)

def chord_method(arr, a, b, eps):

    arr = list(map(lambda x: -x, arr)) if newF(deriv(deriv(arr)), a) < 0 else arr

    if newF(arr, a) > 0:
        fixValue, x = a, b
        necessary_step = first
    else:
        fixValue, x = b, a
        necessary_step = second

    x_1 = necessary_step(arr, fixValue, x)
    while abs(x - x_1) >= eps: 
        x_1 = x
        x = necessary_step(arr, fixValue, x)
    return x


print(chord_method([1, -1, 0, 1], -2, -1, 1e-3))