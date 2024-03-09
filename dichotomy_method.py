def f(x):
    return (x - 1)*(x - 2)*(x - 3)


def dichotomy(f, x0, x1, eps):
    while abs(x1 - x0) >= eps:
        x3 = (x0 + x1) / 2

        if f(x0)*f(x3) <= 0: 
            x1 = x3

        elif f(x1)*f(x3) <= 0:
            x0 = x3

    return x1


print(dichotomy(f=f, x0=2, x1=5, eps=0.01))     
