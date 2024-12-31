import sys
import math
from scipy.optimize import newton

def find_collision_time(data):
    x1, y1, z1, r1, vx1, vy1, vz1 = data[0][0], data[0][1], data[0][2], data[0][3], data[0][4], data[0][5], data[0][6]
    x2, y2, z2, r2, vx2, vy2, vz2 = data[1][0], data[1][1], data[1][2], data[1][3], data[1][4], data[1][5], data[1][6]
    
    # Define the equation using a lambda function
    equation = lambda t: math.sqrt(
        (x2 - x1 + (vx2 - vx1) * t)**2 +
        (y2 - y1 + (vy2 - vy1) * t)**2 +
        (z2 - z1 + (vz2 - vz1) * t)**2
    ) - (r1 + r2)

    # Solve for 't' using Newton's method
    t_collision = newton(equation, x0=0.0)
    t_collision = round(t_collision, 3)

    return t_collision if t_collision > 0 else "No Collision"
    
n = int(sys.stdin.readline())

data = []

for _ in range(n):
    for j in range(2):
        input_string = input()
        numbers = [int(x) for x in input_string.split()]
        data.append(numbers)
    print(find_collision_time(data))
    data = []