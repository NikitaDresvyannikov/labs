import math

def task1():
    x = float(input('Произвольное x:'))
    y = float(input('Произвольное y:'))
    z = float(input('Произвольное z:'))

    a = (3 + (math.e)**2) / (1+(x)**2 * abs(y - math.tan(z)))
    b = 1 + abs(y - x) + ((y - x)**2) / 2 + ((x - y)**2) / 3

    print('a =', a)
    print('b =', b)
task1()

def task2():
    a = -2
    b = 5
    c = 3
    def f(x):
        return (b*x + a)**2 / (c + x**3) + x**4
    print(f())
task2()

def task4():
    a = float(input('Произвольное a:'))
    b = float(input('Произвольное b:'))
    c = float(input('Произвольное c:'))
    if c == (a**2 + b**2)**0.5:
        h = (a * b) / c
        print('h=', h)
    else:
        print('Треугольник не существует')
task4()
