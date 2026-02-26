import numpy as np

import matplotlib.pyplot as plt

q1 = 15000
q2 = 20000
q = 10000
E1 = 2.1 * 10**11
E2 = 2.1* 10**11
E3 = 2.1* 10**11
l = 3
n = 6
u = 10**(-3)
g = 9.81
r1 = 504
r2 = 666
r3 = 228
EPS = 10**(-3)

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
    if abs(x) <= EPS:
        return 1
    else:
        return 0

x_i = np.linspace(0, l, n+1)
h = l/n
E_zn = np.zeros(n+1)
r_zn = np.zeros(n+1)
for i in range(n+1):
    E_zn[i] = E(x_i[i])
    r_zn[i] = r(x_i[i])
print(E_zn)
K = np.zeros((n+1, n+1))
M = np.zeros((n+1,1))
for i in range(1, n):
    K[i][i-1] = (E_zn[i-1])/h**2
    K[i][i] = (-E_zn[i-1] - E_zn[i]) / h ** 2
    K[i][i+1] = (E_zn[i])/h**2
    M[i][0] = r(x_i[i]) * g - q1 * delta(x_i[i] - l/3)/h - q2 * delta(x_i[i] - l/2)/h
M[0][0] = -u
M[n][0] = q
K[0][0] = 1
K[n][n-1] = -E(l) / h
K[n][n] = E(l) / h

# print(M)
peremeshenia = np.linalg.solve(K, M)
sigma = np.zeros(len(peremeshenia))

for i in range(1, n):
    sigma[i] = E_zn[i] * (peremeshenia[i+1]-peremeshenia[i])/h
sigma[0] = E_zn[0]*(peremeshenia[1]-peremeshenia[0])/h
sigma[n] = E_zn[n]*(peremeshenia[n]-peremeshenia[n-1])/h
print(sigma)

plt.plot(x_i, peremeshenia)
plt.grid(True)
plt.show()
# print(K)
print('\n')
# print(peremeshenia)

