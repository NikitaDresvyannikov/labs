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
        return float((b*x + a)**2 / (c + x**3) + x**4)
    print(f())
    
task2()

def task3():
    
    x = float(input('Произвольное x:'))
    def f(x):
        return (abs(math.log((math.cos(x**2))))) / (math.sin(x ** 2 + x ** 0.5))
    print('f(x)=',f(x))
    
task3()

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

def task6():
    
    R = float(input('R-радиус окружности:'))
    a = float(input('a - сторона правильного вписанного многоугольника:'))
    n = float(input('n - кол-во сторон:'))
    
    a2n = math.sqrt(2*R**2-2*R*math.sqrt(R**2-(((a**2) * n)/4)))
    
    print('a2n=', a2n)
    
task6()

def task7():
    
    A1 = float(input('A1='))
    B1 = float(input('B1='))
    C1 = float(input('C1='))
    A2 = float(input('A2='))
    B2 = float(input('B2='))
    C2 = float(input('C2='))
    
    if -10 <= A1 <= 10 and -10 <= A2 <= 10 and -10 <= B1 <= 10 and -10 <= B2 <= 10 and -10 <= C1 <= 10 and -10 <= C2 <= 10:
        D = A1 * B2 - A2 * B1
        x = (C1 * B2 - C2 * B1)/ D
        y = (A1 * C2 - A2 * C1)/ D
        print('x=', x)
        print('y=', round(y, 4))
    else:
        print('Введите числа [-10;10]')
        
task7()

def task8():
    
    Tc = float(input('Введите значение температуры в градусах Цельсия:'))
    if 0 <= Tc <= 100:
        Tf = ((Tc * 9)/5) + 32
        print('Tf=', round(Tf, 4))
    else:
        print('Введите значения [0,100]')
        
task8()

def task9():
    
    x = float(input('Введите рубли:'))
    y = float(input('Введите курс доллара:'))
    z = float(input('Введите процент:'))
    dollars = abs(x / y - ((x / y) * z / 100))
    print('dollars = ', round(dollars, 4))
    
task9()
