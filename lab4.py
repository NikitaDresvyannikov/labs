import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

n = 6
q = 200000
q1 = 100000
q2 = 300000
E1 = 20 * 10 ** 9
E2 = 20 * 10 ** 10
E3 = 20 * 10 ** 11

p1 = 8000
p2 = 8000
p3 = 8000

L = 6
u0 = 0.001
g = 9.81

def delta(x,x0):
    eps = 1e-6
    if abs(x - x0) < eps:
        return 1
    else:
        return 0

def E(x):
    if x <= L / 3:
        return E1
    elif x >= 2 * L / 3:
        return E3
    else:
        return E2

def int_E(x):
    return E(x)

def p(x):
    if x <= L / 3:
        return p1
    elif x >= 2 * L / 3:
        return p3
    else:
        return p2

def N1(x, x0):
    return q1*(x, x0)/2

h = L / n
x = np.linspace(0, L, n + 1)

K = np.zeros((n + 1, n + 1))
F = np.zeros((n + 1, 1))

two = np.zeros((n, 2))



for i in range(0, n):
    two[i, 0] = i
    two[i, 1] = i+1

for i in range(1, n):
    B = [-1/h, 1/h]
    Bt = np.transpose(B)
    D = quad(int_E, x[i], x[i+1])[0]
    Ke = B @ Bt
    Fg = np.array([[p1*g*h/2], [p1*g*h/2]])
    Fq = np.array(([[q1*delta(x, L/3)/2+q2*delta(x, L/2)/2+q*delta(x-L)],[1*delta(x, L/3)/2+q2*delta(x, L/2)/2+q*delta(x-L)]]))
    Fe = Fg + Fq

    for j in range(len(Ke)):
        for k in range(len(Ke[i])):
            K[j+i][k+i] += Ke[j][k]

    for j in range(len(Fe)):
        F[j+i][0] += Fe[j][0]
        


print(Ke)


