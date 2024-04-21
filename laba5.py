# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = [2.3, 3.71, 4.8, 5.9, 6.3, 6.25, 5.87, 4.82, 3.7, 2.2]

# x = [1, 2, 4, 6, 8, 10, 12, 15, 18, 20]
# y = [7.6, 7.2, 6.57, 5.95, 5.45, 5.09, 4.9, 4.6, 4.3, 4.1]

sum_x = sum(x)
sum_x2 = 0
sum_x3 = 0
sum_x4 = 0
sum_y = sum(y)
sum_yx = 0
sum_yx2 = 0

for x_i in x:
    sum_x2 += x_i ** 2
    sum_x3 += x_i ** 3
    sum_x4 += x_i ** 4
for i in range(len(x)):
    sum_yx += y[i] * x[i]
    sum_yx2 += y[i] * x[i]**2


def treug_determinant(m):
    return m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[0][2] * m[1][0] * m[2][1] \
            - m[0][2] * m[1][1] * m[2][0] - m[0][1] * m[1][0] * m[2][2] - m[0][0] * m[1][2] * m[2][1]


matrix_coeff = [len(x), sum_x, sum_x2], [sum_x, sum_x2, sum_x3], [sum_x2, sum_x3, sum_x4]
matrix_svobodnihchl = [sum_y, sum_yx, sum_yx2]
submatrix1 = [matrix_svobodnihchl, matrix_coeff[1], matrix_coeff[2]]
submatrix2 = [matrix_coeff[0], matrix_svobodnihchl, matrix_coeff[2]]
submatrix3 = [matrix_coeff[0], matrix_coeff[1], matrix_svobodnihchl]
determinant = treug_determinant(matrix_coeff)
a = treug_determinant(submatrix1) / determinant
b = treug_determinant(submatrix2) / determinant
c = treug_determinant(submatrix3) / determinant
# print(a, b, c)
x_n = int(input('Введите время:\n'))
y_n = a + b * x_n + c * x_n ** 2
print(round(y_n, 2))
# print(matrix_coeff, matrix_svobodnihchl)
# print(sum_x)
