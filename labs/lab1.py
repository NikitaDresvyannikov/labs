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

def task5():
    x1 = float(input('x1='))
    y1 = float(input('y1='))
    z1 = float(input('z1='))
    x2 = float(input('x2='))
    y2 = float(input('y2='))
    z2 = float(input('z2='))
    x3 = float(input('x3='))
    y3 = float(input('y3='))
    z3 = float(input('z3='))
    F1 = [x1,y1,z1]
    F2 = [x2,y2,z2]
    F3 = [x3,y3,z3]
    F = [x1+x2+x3,y1+y2+y3,z1+z2+z3]
    print('F=', F)
task5()
