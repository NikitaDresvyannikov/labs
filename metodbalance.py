import numpy as np
from numpy import trapz
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Параметры из метода конечных разностей
L = 1.0  # Длина стержня
P1 = 20000  # Нагрузка в точке L/3 (аналог Q1)
P2 = 70000  # Конечная нагрузка (аналог Q2)
RG = 78000  # Плотность материала (аналог граничного усилия)
E1, E2, E3 = 2e11, 2e12, 2e13  # Модули упругости для разных участков
g = -9.8
# Значения n из метода конечных разностей (grids = [7, 49, 99])
k = 3
n = [7, 49, 99]  # Используем те же сетки, что и в методе конечных разностей

eps = 1e-10


# Функции материала (адаптированные под три участка)
def rg(x):
    return RG + 0 * x  # Используем RG из метода конечных разностей


def E(x):
    """Кусочно-постоянный модуль упругости для трех участков"""
    return np.where(x <= L / 3, E1,
                    np.where(x <= 2 * L / 3, E2, E3))


def invE(x):
    return 1 / E(x)


def P(xx, h):
    """Функция нагрузки с одной точкой приложения"""
    return np.where(np.abs(xx - L / 3) <= eps, P1 / h, 0)


# Инициализация результатов
U = []
sigma_all = []
pogrr = np.zeros(k - 1)

plt.figure(1, figsize=(10, 5))
plt.figure(2, figsize=(10, 5))

for t in range(k):
    h = L / (n[t] - 1)
    x = np.linspace(0, L, n[t])

    # Вычисляем коэффициенты a
    a = np.zeros(n[t])
    for p in range(n[t] - 1):
        integral, _ = quad(invE, x[p], x[p + 1])
        a[p] = h / max(integral, 1e-20)

    a[-1] = E3  # Используем E3 для последнего элемента

    # Построение матрицы A
    A = np.zeros((n[t], n[t]))
    b = np.zeros(n[t])

    # Граничные условия
    A[0, 0] = 1
    A[-1, -1] = a[-1] / h
    A[-1, -2] = -a[-1] / h

    # Основная часть матрицы
    for i in range(1, n[t] - 1):
        A[i, i] = -a[i] / h - a[i - 1] / h
        A[i, i + 1] = a[i] / h
        A[i, i - 1] = a[i - 1] / h

    # Вектор правой части
    for i in range(1, n[t] - 1):
        xcmin = (x[i - 1] + x[i]) / 2
        xcmax = (x[i + 1] + x[i]) / 2
        xx = np.linspace(xcmin, xcmax, 101)
        hx = xx[1] - xx[0]
        b[i] = np.trapz(P(xx, hx), xx) - quad(rg, xcmin, xcmax)[0]

    b[0] = 0
    b[-1] = P2  # Используем P2 (аналог Q2) как граничное условие

    # Решение системы
    try:
        U1 = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        U1 = np.linalg.lstsq(A, b, rcond=None)[0]

    # Расчет напряжений
    sigma = np.zeros(n[t])
    sigma[1:-1] = a[1:-1] * (U1[2:] - U1[1:-1]) / h
    sigma[0] = a[0] * (U1[1] - U1[0]) / h
    sigma[-1] = a[-1] * (U1[-1] - U1[-2]) / h

    U.append(U1)
    sigma_all.append(sigma)

    # Графики
    plt.figure(1)
    plt.plot(x, U1, label=f'n={n[t]}')

    plt.figure(2)
    plt.plot(x, sigma, label=f'n={n[t]}')

# Расчет погрешностей между сетками 7-49 и 49-99
for i in range(k - 1):
    # Для сравнения разных сеток используем только общие точки
    step = n[i + 1] // n[i]
    common_points = min(n[i], n[i + 1] // step)
    err = U[i][:common_points] - U[i + 1][::step][:common_points]
    pogrr[i] = np.sqrt(np.sum(err ** 2) / common_points)

# Оформление графиков
plt.figure(1)
plt.grid(True)
plt.title('Перемещения U (метод баланса)')
plt.xlabel('x')
plt.ylabel('U')
plt.legend()

plt.figure(2)
plt.grid(True)
plt.title('Напряжения sigma (метод баланса)')
plt.xlabel('x')
plt.ylabel('sigma')
plt.legend()

plt.figure(3, figsize=(10, 5))
plt.plot(range(1, k), pogrr, 'o-')
plt.grid(True)
plt.title('Погрешность между решениями (7-49 и 49-99 точек)')
plt.xlabel('Пары сеток (n[i] и n[i+1])')
plt.ylabel('Норма погрешности')

plt.tight_layout()
plt.show()
