import math
import numpy as np


def task1():
    x = float(input('Введите произвольное x\n'))
    # Ввод произвольного x
    y = float(input('Введите произвольное y\n'))
    # Ввод произвольного y
    z = float(input('Введите произвольное z\n'))
    # Ввод произвольного z

    a = (3 + math.e ** 2) / (1 + x ** 2 * abs(y - math.tan(z)))
    # Вычисление значения a
    b = 1 + abs(y - x) + ((y - x) ** 2) / 2 + ((x - y) ** 2) / 3
    # Вычисление значения b

    print('a =', a)
    # Вывод значения a
    print('b =', b)
    # Вывод значения b


try:
    task1()
except ZeroDivisionError:
    print("делить на ноль нельзя")
    exit(0)


def task2():
    a = -2
    # Значение a из условия задания
    b = 5
    # Значение b из условия задания
    c = 3
    # Значение c из условия задания
    x = float(input('Введите произвольное x\n'))
    # Ввод произвольного значения x

    f = (b * x + a) ** 2 / (c + x ** 3) + x ** 4
    # Вычисление значения функции

    print('f(x)=', f)
    # Вывод значения функции


try:
    task2()
except ZeroDivisionError:
    print("делить на ноль нельзя")
    exit(0)


def task3():
    x = float(input('Введите произвольное x\n'))
    # Ввод произвольного х
    f1 = abs(math.log((math.cos(x ** 2))))
    f2 = math.sin(x ** 2 + x ** 0.5)
    f = f1 / f2
    # Вычисление значения функции

    print('f(X)=', f)
    # Вывод значения функции


try:
    task3()
except ZeroDivisionError:
    print("делить на ноль нельзя")
    exit(0)
except ValueError:
    print("логарифм <= 0")
    exit(0)


def task4():
    catet_a = float(input('Введите катет a\n'))
    # Ввод произвольного катета a
    catet_b = float(input('Введите катет b\n'))
    # Ввод произвольного катета b
    gipotinuza_c = float(input('Введите гипотинузу c\n'))
    # Ввод произвольной гипотинузы c

    if gipotinuza_c == (catet_a ** 2 + catet_b ** 2) ** 0.5:
        # Проверка существует ли прямоугольный треугольник

        visota_h = (catet_a * catet_b) / gipotinuza_c
        # Вычисление высоты прямоугольного треугольника
        print('Высота треугольника равна h=', visota_h)
        # Вывод высоты прямоугольного треугольника
    else:
        print('Прямоугольный треугольник не существует')
        # Вывод сообщения, что такого прямоугольного треугольника не существует


def task5():
    coord_f1 = [int(input('Введите x1\n')), int(input('Введите y1\n')), int(input('Введите z1\n'))]
    coord_f2 = [int(input('Введите x2\n')), int(input('Введите y2\n')), int(input('Введите z2\n'))]
    coord_f3 = [int(input('Введите x3\n')), int(input('Введите y3\n')), int(input('Введите z3\n'))]
    # Ввод произвольных x1,y1,z1,x2,y2,z2,x3,y3,z3 и создание списка

    vector_sili_f1 = np.array(coord_f1)
    # Создание массива
    vector_sili_f2 = np.array(coord_f2)
    # Создание массива
    vector_sili_f3 = np.array(coord_f3)
    # Создание массива

    ravnodeystv_sila_f = vector_sili_f1 + vector_sili_f2 + vector_sili_f3
    # Находим координаты равнодействующей силы

    print('ravnodeystv_sila_F =', ravnodeystv_sila_f)
    # Вывод равнодействующей силы


def task6():
    radius_R = float(input('Введите радиус окружности\n'))
    # Ввод произвольного значения радиуса окружности
    storona_a = float(input('Введите значение стороны правильного вписанного многоугольника\n'))
    # Ввод произвольного значения стороны правильного вписанного многоугольника
    count_n = float(input('Введите количество сторон многоугольника\n'))
    # Ввод количества сторон многоугольника

    a2n = math.sqrt(2 * radius_R ** 2 - 2 * radius_R * math.sqrt(radius_R ** 2 - (((storona_a ** 2) * count_n) / 4)))
    # Вычисление стороны правильного вписанного многоугольника с удвоенным числом сторон

    print('a2n=', a2n)
    # Вывод стороны правильного вписанного многоугольника с удвоенным числом сторон


def task7():
    a1 = float(input('Введите A1\n'))
    b1 = float(input('Введите B1\n'))
    c1 = float(input('Введите C1\n'))
    # Ввод произвольных значений A1,B1,C1
    a2 = float(input('Введите A2\n'))
    b2 = float(input('Введите B2\n'))
    c2 = float(input('Введите C2\n'))
    # Ввод произвольных значений A2,B2,C2

    if -10 <= a1 <= 10 and -10 <= a2 <= 10 and \
            -10 <= b1 <= 10 and -10 <= b2 <= 10 \
            and -10 <= c1 <= 10 and -10 <= c2 <= 10:
        # Проверяем находятся ли A1,B1,C1,A2,B2,C2 на промежутке [-10;10]
        d = a1 * b2 - a2 * b1
        # Вычисляем значение D
        x = (c1 * b2 - c2 * b1) / d
        # Вычисляем значение x
        y = (a1 * c2 - a2 * c1) / d
        # Вычисляем значение y

        print('x =', x)
        # Вывод значения x
        print('y =', round(y, 4))
        # Вывод значения y, с точностью до 4 цифр в дробной части
    else:
        print('Введите числа [-10;10]')
        # Вывод ошибки


try:
    task7()
except ZeroDivisionError:
    print("делить на ноль нельзя")
    exit(0)


def task8():
    temperature_celsia = float(input('Введите Температуру Цельсия\n'))
    # Ввод произвольного значения Температуры Цельсия
    if 0 <= temperature_celsia <= 100:
        # Проверяем соответсвует ли введённое значение промежутку [0;100]
        temperature_farengeita = ((temperature_celsia * 9) / 5) + 32
        # Вычисляем значение температуры Фаренгейта
        print('tf =', round(temperature_farengeita, 4))
        # Выводим значение температуры Фаренгейта с точностью до 4 цифр в дробной части
    else:
        print('Введите значения [0,100]\n')
        # Вывод ошибки


def task9():
    rubles = float(input('Введите сумму рублей:\n'))
    # Ввод произвольного значения суммы в рублях
    curse_dollars = float(input('Введите курс доллара:\n'))
    # Ввод курса доллара
    comissiya = float(input('Введите процент:\n'))
    # Ввод комиссии
    dollars = abs(rubles / curse_dollars * (1 - comissiya / 100))
    # Перевод рублей в доллары
    print('dollars = ', round(dollars, 4))
