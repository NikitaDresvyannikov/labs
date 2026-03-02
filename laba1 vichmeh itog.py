import numpy as np
import matplotlib.pyplot as plt


q = 50000
q1 = 10000
q2 = 10000
E1 = 5 * 10 ** 11
E2 = 1 * 10 ** 11
E3 = 3 * 10 ** 11

r1 = 700
r2 = 500
r3 = 600

l = 7
n = 12
u = 0.001
g = 9.81

EPS = 1e-6

def E(x):
    if x <= l/3:
        return E1
    elif x >= 2 * l/3:
        return E3
    else:
        return E2

def r(x):
    if x <= l / 3:
        return r1
    elif x >= 2 * l / 3:
        return r3
    else:
        return r2

def delta(x):
    if abs(x - l / 3) < EPS or abs(x - l / 2)< EPS:
        return 1
    else:
        return 0

Gn_U = []
n_val = []
h = []
for k in range(3):
    nn = n * 2**k
    x_i = np.linspace(0, l, nn+1)
    h.append(l/nn)
    K = np.zeros((nn+1, nn+1))
    M = np.zeros(nn+1)
    for i in range(1, nn):
        K[i][i-1] = (E(x_i[i]))/h[k]**2
        K[i][i] = (-E(x_i[i+1]) - E(x_i[i])) / h[k] ** 2
        K[i][i+1] = (E(x_i[i+1]))/h[k]**2
        M[i] = r(x_i[i]) * g - q1 * delta(x_i[i])/h[k] - q2 * delta(x_i[i])/h[k]
    M[0] = -u
    M[nn] = q
    K[0][0] = 1
    K[nn][nn-1] = -E(x_i[nn]) / h[k]
    K[nn][nn] = E(x_i[nn]) / h[k]


    U = np.linalg.solve(K, M)
    sigma = np.zeros(nn+1)

    for i in range(nn):
        sigma[i] = E(x_i[i]) * (U[i+1]-U[i])/h[k]
    sigma[0] = E(x_i[0])*(U[1]-U[0])/h[k]
    sigma[nn] = E(x_i[nn])*(U[nn]-U[nn-1])/h[k]

    gilbu = np.sqrt(np.sum((U**2) * h[k]))
    Gn_U.append(gilbu)

    n_val.append(nn)

    plt.plot(x_i, U, marker='*', color='black')
    plt.grid(True)
    plt.title('Изменение перемещений по длине стержня')
    plt.xlabel('x')
    plt.ylabel('U')
    plt.show()

    plt.plot(x_i, sigma, marker='o', color='black')
    plt.grid(True)
    plt.grid(True)
    plt.title('Изменение напряжений по длине стержня')
    plt.xlabel('x')
    plt.ylabel('sigma')
    plt.show()

for i in range(len(n_val)):
    print(f"n = {n_val[i]}: {Gn_U[i]:.4e}")
print('\n')


# print('Перемещения')
# for prnt1 in U:
#     print("{:.4e}".format(prnt1))
#
# print('\n')
#
# print('Напряжения')
# for prnt2 in sigma:
#     print("{:.4e}".format(prnt2))
