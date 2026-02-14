import numpy as np

def f(x):
    return np.tan(x)**2

def df(x):
    return (2*np.tan(x))/(np.cos(x))**2

x_0 = 1.4
h = 0.1

pogr = []

for i in range(4):
    y_left = (f(x_0) - f(x_0 - h))/ h
    y_right = (f(x_0) + f(x_0 + h))/ h
    y_central = (f(x_0 + h) - f(x_0 - h))/(2*h)

    pogr_left = abs((df(x_0)-y_left)/df(x_0))
    pogr_right = abs((df(x_0)-y_right)/df(x_0))
    pogr_central = abs((df(x_0)-y_central)/df(x_0))
    pogr.append((pogr_left,pogr_right,pogr_central))

    h/=2

for j in range(len(pogr)):
    for k in range(len(pogr[j])):
        print(f'{pogr[j][k]:.4e} ',end='')
    print('\n')
