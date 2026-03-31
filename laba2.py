import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

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
n = 24
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

def heaviside(x):
    if x >= 0:
        return 1
    else:
        return 0

def a(x):
    return 1/E(x)

x_i = np.linspace(0, l, 2*n+1)
h=l/n
K = np.zeros((n+1, n+1))
M = np.zeros(n+1)
for i in range(1, n):
    K[i][i-1] = integrate.quad(a,x_i[2*(i-1)], x_i[2*i])[0]
    K[i][i] = -integrate.quad(a, x_i[2*(i-1)], x_i[2*i])[0]-integrate.quad(a, x_i[2*i], x_i[2*(i+1)])[0]
    K[i][i+1] = integrate.quad(a, x_i[2*(i)], x_i[2*(i+1)])[0]
    M[i] = integrate.quad(r, x_i[i-1], x_i[i+1])[0] * g - q1 * (heaviside(x_i[i+1] - l/3)-heaviside(x_i[i-1] - l/3))- q2 * (heaviside(x_i[i+1] - l/2)-heaviside(x_i[i-1] - l/2))
M[0] = -u
M[n] = q
K[0][0] = 1
K[n][n-1] = -integrate.quad(a, x_i[2*(n-1)], x_i[2*n])[0]
K[n][n] = integrate.quad(a, x_i[2*(n-1)], x_i[2*n])[0]
sigma = np.zeros(n+1)
U = np.linalg.solve(K, M)
for i in range(n):
    sigma[i] = E(x_i[i]) * (U[i+1]-U[i])/h
sigma[0] = E(x_i[0])*(U[1]-U[0])/h
sigma[n] = E(x_i[n])*(U[n]-U[n-1])/h

# plt.plot(x_i[0:2*n+1:2], U, marker='*', color='black')
# plt.grid(True)
# plt.title('Изменение перемещений по длине стержня')
# plt.xlabel('x')
# plt.ylabel('U')
# plt.show()
plt.plot(x_i[0:2*n+1:2], sigma, marker='*', color='black')
plt.grid(True)
plt.title('graphic')
plt.xlabel('x')
plt.ylabel('sigma')
plt.show()
# print(U)
print(sigma)
