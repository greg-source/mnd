import random

A0=0
A1=1
A2=2
A3 = 3


def x_generator(start=1, stop=20):
    num_list = [[random.randrange(start, stop) for j in range(8)] for i in range(3)]
    return num_list


def y_generator(x_list, A0=0, A1=1, A2=2, A3=3):
    return [A0 + A1 * x_list[0][i] + A2 * x_list[1][i] + A3 * x_list[2][i] for i in range(8)]


def x0_generator(x_list):
    return [(max(i) + min(i)) / 2 for i in x_list]


def dx_generator(x_list):
    return [max(x_list[i]) - x0_generator(x_list)[i] for i in range(3)]


def xn_generator(x_list, x0_list, dx_list):
    xn_list = [[(x_list[i][j] - x0_list[i]) / dx_list[i] for j in range(8)] for i in range(3)]
    return xn_list


a = x_generator()
b = xn_generator(a, x0_generator(a), dx_generator(a))

print('Варіант 205')
print('  X1|      X2|      X3|       Y|     Xn1|     Xn2|     Xn3|')
print('-' * 59)
for i in range(8):
    print(
        "{0:4}|{1:8}|{2:8}|{3:8}|{4:8.2}|{5:8.2}|{6:8.2}|".format(a[0][i], a[1][i], a[2][i],
                                                                  y_generator(a)[i], b[0][i], b[1][i], b[2][i]))

print('\n|X0: {0:7} {1:7} {2:7}|'.format(*x0_generator(a)))
print('|dx: {0:7} {1:7} {2:7}|'.format(*dx_generator(a)))
y_et = A0 + A1 * x0_generator(a)[0] + A2 * x0_generator(a)[1] + A3 * x0_generator(a)[2]
print('Yет = {0}'.format(y_et))
print('max((Y - Yeт)^2)={0}'.format((max(y_generator(a)) - y_et) ** 2))
print("Виконав: студент Грициняк Г.С.")
