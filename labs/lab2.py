import matplotlib.pyplot as plt
import numpy as np
import math


def task1():
    def func1(x):
        if (x % 10)%2 == 0:
            return True
        else:
            return False


    def func2(x):
        if x > 0:
            return True
        else:
            return False

    x = float(input('Введите число x\n'))
    if func1(x):
        print("Число оканчивается на чётную цифру")
    else:
        print("Число не оканчивается на чётную цифру")
    if func2(x):
        print('Число x является положительным')
    else:
        print("Число x не является положительным")


def task2():
    def f(x):
        if x >= 0:
            return 2 * x ** 3 - 2
        if x < 0:
            return -(math.sin(x))


    a = int(input('Введите значение a\n'))
    b = int(input('Введите значение b\n'))
    vector_x = [x for x in range(a, b+1)]
    vector_y = [f(x) for x in range(a, b+1)]
    plt.plot(vector_x, vector_y)
    plt.grid(True)
    plt.show()


def task3():
    number = float(input('Введите число:\n'))
    base = int(input('Введите основание новой СС:\n'))


    def decimnal_in_new_numeral_system(number, base):
        result = ''
        while number > 0:
            number_2 = int(number * base)
            if number_2 >= base:
                number_2 = number_2 - 1
            result += str(number_2)
            number = (number * base) % 1
        return result


    new_number = decimnal_in_new_numeral_system(number, base)

    print('Новое число:\n', new_number)

import matplotlib.pyplot as plt
import numpy as np


def task4():
    alpha = np.linspace(0, np.pi, 150)

    radius = 2

    a1 = radius * np.cos(alpha) - 1
    b1 = radius * np.sin(alpha) + 3
    x1 = [1,1,0,-3]
    y1 = [3,1,-1,3]
    ax = plt.subplot()
    ax.plot(a1, b1, color='black')
    ax.plot(x1, y1, color='black')
    ax.set_aspect(1)

    alpha2 = np.linspace(np.pi, 2*np.pi, 150)
    radius = 2

    a2 = radius * np.cos(alpha2) + 5
    b2 = radius * np.sin(alpha2)
    x2=[3,5,7]
    y2=[0,2,0]
    ax.plot(a2, b2, color='black')
    ax.plot(x2, y2, color='black')
    plt.grid()
    plt.title('Task 4')
    plt.show()
def popadanie_tochki(x, y, polygon):
    n = len(polygon)
    inside = False
    
    p1x, p1y = polygon[0]
    for i in range(n+1):
        p2x, p1y = polygon[i % n]
        if y > min(p1y)
        
task4()

def task5():
    pr = 1
    cnt = 0
    while cnt != 4:
        x = float(input('Введите отрицательное число\n'))
        if x < 0:
            pr *= x
            cnt += 1
        if x > 0:
            print('Ошибка!\t')
        if cnt == 4:
            if pr < 0:
                print('Произведение отрицательно\n', pr)
            if pr > 0:
                print('Произведение положительно\n', pr)


def task6():
    def func_finobacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return func_finobacci(n - 1) + func_finobacci(n - 2)
    rabbits = 1
    for month in range(1, 12 + 1):
        rabbits += func_finobacci(month)
    print(rabbits)


def task8():
    def possledovatelnost(n, x):
        result = 0
        for i in range(0, n + 1):
            result += (i + 1) * (x ** (n - i))
            # ??????????
        return result
    n = int(input('Введите n:'))
    x = int(input('Введите x:'))
    print(possledovatelnost(n,x))


def task9():
    sum1 = 0

    for i in range(1, 8 + 1):
        for j in range(1, i + 1):
            j_itog = j ** 2
            sum1 += j_itog
    print('Ответ первого выражения:',sum1)

    sum2 = 0
    pr = 1

    for i in range(1, 8 + 1):
        for j in range(1, i + 1):
            pr *= (j + i)*(j - i)
            sum2 += pr
    print('Ответ второго выражения:',sum2)

    sum3 = 0
    for i in range(1, 8 + 1):
        for j in range(1, i + 1):
            for k in range(1, i + j + 1):
                k_itog = j ** 2 + i + k
                j_itog = k_itog
                sum3 += j_itog
    print('Ответ третьего выражения:',sum3)


import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.sin(x) - x**2


def grafik():

    axes = plt.subplot()
    x_vector = np.linspace(1, 2, 100)
    y_vector = f(x_vector)
    axes.plot(x_vector, y_vector, color='red')
    axes.plot([1,2], [0,0], color='k')
    axes.plot([1,1], [0, f(1)], color='k', linestyle= '--')
    axes.plot([2,2], [0,f(2)], color = 'gray')
    plt.show()


def area_figure(a,b, n = 100000):
    h = (b - a) / n
    x_i = []
    for multiplier in range(n):
        x_i.append(a+(h * multiplier))

    area = 0
    for i in range(1,len(x_i)):
        area += (f(x_i[i]) + f(x_i[i-1]))/2 * h
    if area > 0:
        print(area)
    else:
        print(abs(area))


area_figure(1,2)
grafik()
