import math
import matplotlib.pyplot as plt

def method(x_values, y_values, x_target):
    try:
        for i, x in enumerate(x_values):
            if x > x_target:
                x2 = x
                x1 = x_values[i - 1]
                y2 = y_values[i]
                y1 = y_values[i - 1]
                
                # Linear interpolation
                y_target = y1 + (y2 - y1) / (x2 - x1)  * (x_target - x1)
                print(f"For x = {x_target}, y = {y_target}")
                
                plt.plot(x_values, y_values, marker='*')
                plt.plot([x_target, x_target], [0 , y_target], 'r--')
                
                plt.xlim([0, x_values[-1] * 1.1])
                plt.ylim([0, y_values[-1] * 1.1])

                plt.grid()
                plt.show()
                break
        else:
            print(f"Given x_target = {x_target} is out of range")
    except:
        print("Some problem occurs.")