import numpy as np

def f(x):
    return np.tan(x)**2

def df(x):
    return (2*np.tan(x))/(np.cos(x))**2

def df2(x):
    return (4 * (np.sin(x))**2 + 2)/(np.cos(x))**4

a = 0.1
b = 1.5
n = 30
n_cheb = []
n_gilb = []

for _ in range(4):
    h = (b - a)/n
    n_cheb_left = 0
    n_cheb_right = 0
    n_cheb_central = 0
    n_cheb_dy2 = 0
    n_gilb_left = 0
    n_gilb_right = 0
    n_gilb_central = 0
    n_gilb_dy2 = 0
    for i in range(1, n):
        x_i = h * i
        y_left = (f(x_i) - f(x_i - h))/h
        y_right = (f(x_i + h) - f(x_i))/h
        y_central = (f(x_i + h) - f(x_i - h))/(2 * h)

        dy2 = (f(x_i - h) - 2 * f(x_i) + f(x_i + h))/(h**2)
        n_cheb_dy2 = max(n_cheb_dy2, abs(df2(x_i) - dy2))
        n_gilb_dy2 += ((df2(x_i) - dy2)**2) * (1/n)


        n_cheb_left = max(n_cheb_left, abs(df(x_i) - y_left))
        n_cheb_right = max(n_cheb_right, abs(df(x_i) - y_right))
        n_cheb_central = max(n_cheb_central, abs(df(x_i) - y_central))
        n_gilb_left += ((df(x_i) - y_left) ** 2) * (1 / n)
        n_gilb_right += ((df(x_i) - y_right) ** 2) * (1 / n)
        n_gilb_central += ((df(x_i) - y_central) ** 2) * (1 / n)

    n_cheb.append((n_cheb_left, n_cheb_right, n_cheb_central, n_cheb_dy2))
    n_gilb.append((n_gilb_left, n_gilb_right, n_gilb_central, n_gilb_dy2))
    n *= 2
for i in range(len(n_cheb)):
    print(*n_cheb[i])
print('\n')
for i in range(len(n_gilb)):
    print(*np.sqrt(n_gilb[i]))

