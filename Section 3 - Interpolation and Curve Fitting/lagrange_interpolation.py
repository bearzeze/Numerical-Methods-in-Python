import math


def method(x_values, y_values, degree):
    x_target = float(input("Enter number: "))
    
    m = len(x_values)
    degree = m - 1
    
    if degree != m - 1:
        print(f"Polynomial degree of {degree} requires {m} elements in x list!")
        return
    
    y_target = 0
    for i in range(0, len(x_values)):
        y_target += y_values[i] * lagrangian(i, x_values, x_target)
        
    print(f"For x = {x_target}, y = {y_target}")

        
def lagrangian(i, x, x_target):
    L = 1 
    for j in range(0, len(x)):
        if i != j:
            L *= (x_target - x[j]) / (x[i] - x[j])
    
    return L