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

