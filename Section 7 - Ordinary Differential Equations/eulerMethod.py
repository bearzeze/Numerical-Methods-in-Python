import numpy as np


def main():
    x = np.linspace(0, 2, 10)
    y = np.zeros(len(x))

    y[0] = 1
    h = x[1] - x[0]
    print(f"x \t\t y_euler \t\t y_analytical ")
    print(f"{format(x[0], '.5f')} \t\t {format(y[0], '.5f')} \t\t {format(y_ana(x[0]), '.5f')}")

    for i in range(1, len(x)):
        y[i] = y[i - 1] + dy(x[i - 1], y[i - 1]) * h
        print(f"{format(x[i] , '.5f')} \t\t {format(y[i] , '.5f')} \t\t {format(y_ana(x[i]) , '.5f')}")


def dy(x, y):
    return x * y

def y_ana(x):
    return np.exp(x**2 / 2)


main()