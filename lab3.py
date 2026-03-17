import numpy as np
# import matplotlib as plt
# import matplotlib.ticker as ticker

L = 2
"""м"""
T0 = 4
"""с"""
k = 50
"""Вт/(м*К)"""
C = 460
"""Дж/(кг*К)"""
rho = 7850
"""кг/м**3"""
a = np.sqrt(k/(rho*C))
Nx = 21
Nt = 500
sigma = 0.5

def alfa(x):
    return 273
def betta(t):
    return 273
def gamma(t):
    return 273
def f(t, x):
    return t * np.cos(x)

for k in range(1, 1):
    U = np.zeros((Nx+1, Nt+1))
    hx = 1/Nx
    ht = (hx ** 2) / (2 - 4 * sigma)
    tau = T0/Nt
    x = np.linspace(0, 1, Nx + 1)
    t = np.arange(0, T0, Nt + 1)
    for i in range(0, Nx + 1):
        U[i, 0]=alfa(x[i])
    for j in range(1, Nt+1):
        K = np.zeros((Nx + 1, Nx + 1))
        F = np.zeros((Nx + 1, 1))
        K[0, 0] = 1
        K[Nx, Nx] = 1
        F[0, 0] = betta(t[j])
        F[Nx, 0] = gamma(t[j])
        print(K)
        for i in range(1, Nx):
            K[i, i - 1] = sigma/hx**2
            K[i, i] = -1/ht-(2*sigma)/hx**2
            K[i, i + 1] = sigma/hx**2
            F[i, 0] = (-(1-sigma)*(U[i-1, j-1]-2*U[i, j-1]+ U[i+1, j-1])/hx**2)-(U[i-1, j]/tau)+f(sigma*t[j]+(1-sigma)*t[j-1], x[i])
            u = np.linalg.solve(K, F).flatten()
            for i in range(0, Nx + 1):
                U[i, j] = u[i]
