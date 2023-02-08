import numpy as np


def main():
    x = np.linspace(0, 2, 10)
    y = np.zeros(len(x))

    y[0] = 1
    h = x[1] - x[0]
    print(f"x \t\t y_RK2 \t\t y_analytical ")
    print(f"{format(x[0], '.5f')} \t\t {format(y[0], '.5f')} \t\t {format(y_ana(x[0]), '.5f')}")


    for i in range(1, len(x)):
        K1 = h * dy(x[i - 1], y[i - 1])
        K2 = h * dy(x[i - 1] + h/2, y[i - 1] + 1/2 * K1)
        y[i] = y[i - 1] + K2
        print(f"{format(x[i] , '.5f')} \t\t {format(y[i] , '.5f')} \t\t {format(y_ana(x[i]) , '.5f')}")


def dy(x, y):
    return x * y


def y_ana(x):
    return np.exp(x**2 / 2)


main()