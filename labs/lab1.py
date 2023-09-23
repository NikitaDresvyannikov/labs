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
