# Praktikum Komnum
# KELOMPOK 7
# 5025211185 / Rano Noumi Sulistyo
# 5025211226 / Sony Hermawan
# 5025201052 / Abisha Kean Tuana Sirait

# IMPORT
import matplotlib.pyplot as plt
import numpy as np

# Bolzano Function


def bolzano(x0, x1, er, a, b, c, d, e, f):
    x2 = 0
    times = 1
    print('\n\nMetode Bolzano')
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print('Iterasi-%d, x3 = %0.6f dan f(x2) = %0.6f' %
              (times, x2, func(x2, a, b, c, d, e, f)))

        if func(x0, a, b, c, d, e, f) * func(x2, a, b, c, d, e, f) < 0:
            x1 = x2
        else:
            x0 = x2
        print('x1= %0.6f dan x2 = %0.6f \n' % (x0, x1))
        times = times + 1
        condition = abs(func(x2, a, b, c, d, e, f)) > er

    print('\n Akar persamaan adalah : %0.8f' % x2)
    return x2

# Function


def func(x, a, b, c, d, e, f):
    return a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f

# Main Function


def main():
    print('Bolzano persamaan polinomial tertentu (max=5)')
    p = int(input('Orde polinomial: '))
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0

    for i in range(p, -1, -1):
        if i == 5:
            a = float(input('variabel pangkat 5: '))
        if i == 4:
            b = float(input('variabel pangkat 4: '))
        if i == 3:
            c = float(input('variabel pangkat 3: '))
        if i == 2:
            d = float(input('variabel pangkat 2: '))
        if i == 1:
            e = float(input('variabel pangkat 1: '))
        if i == 0:
            f = float(input('variabel bebas : '))

    x0 = input('x1: ')
    x1 = input('x2: ')
    er = input('Error: ')

    x0 = float(x0)
    x1 = float(x1)
    x2 = 0
    er = float(er)

    if func(x0, a, b, c, d, e, f) * func(x1, a, b, c, d, e, f) > 0.0:
        print('Akar tidak ada diantara kedua nilai')
        print('coba lagi')
        return
    else:
        x2 = bolzano(x0, x1, er, a, b, c, d, e, f)

    print('\n Plot : %0.8f' % x2)

# Plotting
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    xlist = np.linspace(-10, 10, 100)
    ylist = func(xlist, a, b, c, d, e, f)

    plt.plot(xlist, ylist)
    plt.title("Bolzano")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.show()


if __name__ == "__main__":
    main()
