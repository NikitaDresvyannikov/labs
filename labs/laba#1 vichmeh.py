import numpy as np
# import matplotlib.pyplot as plt

q1 = 500
q2 = 600
q = 1000
E1 = 150/10**11
E2 = 300/10**11
E3 = 600/10**11
l = 5
n = 5
u0 = 0.01
g = 9.81
r1 = 150
r2 = 300
r3 = 600
A = 10

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



x_i = np.linspace(0, l, n)
h = l/(n-1)
E_zn = np.zeros(n)
r_zn = np.zeros(n)
for i in range(n):
    E_zn[i] = E(x_i[i])
    r_zn[i] = r(x_i[i])
K = np.zeros((n+1, n+1))
M = np.zeros((n+1,1))
for i in range(1, n):
    K[i][i-1] = (A * E_zn[i])/h**2
    K[i][i] = (-A * E_zn[i] - A * E_zn[i-1]) / h ** 2
    K[i][i+1] = (A * E_zn[i])/h**2
    M[i][0] = -r(x_i[i]) * g
    if i == np.argmin(abs(x_i - l/3)):
        M[i][0] += q1/h
    if i == np.argmin(abs(x_i - l/2)):
        M[i][0] += q2/h
M[0][0] = -u0
M[n][0] = q
K[0][0] = 1
K[n][n-1] = -E(l) / h
K[n][n] = E(l) / h

solve = np.linalg.solve(K, M)
print(solve)
