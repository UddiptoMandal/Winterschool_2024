import math
import numpy as np

x = 7.0
a = 3.0
b = 4.0
err = 8.0001

# Use numpy.arange for float ranges
for y in np.arange(0.0, 0.5, 0.01):
    B = math.atan2(x, y)
    
    for A in range(180):
        A1 = math.radians(A)
        asin_arg = a * math.sin(A1 - B) / b

        # Check if asin_arg is within [-1, 1]
        if -1 <= asin_arg <= 1:
            expr_value = math.hypot(x, y) - a * math.cos(A1 - B) + b * math.cos(math.asin(asin_arg))
            if abs(expr_value) < err:
                print(f"y = {y:.2f}, Angles A (in degrees) that satisfy the condition:")
                print("A: ", A)
    
                print("B: ", B)
                theta = A - 2*B
                print("Theta: ", theta)
            

