from scipy.optimize import linprog
import numpy as np

# Set up values relating to both minimum and maximum values of y
butter_coeff = [[1, 1, 5, 3]]  # x + y + 5u + 3v <= 50
butter_constant = [50]

flour_coeff = [[2, 2, 1, 1]]  # 2x + 2y + u + v <= 130
flour_constant = [130]

yeast_coeff = [[1, 1, 1, 4]]  # x + y + u + 4v <= 70
yeast_constant = [70]

salt_coeff = [[3, 4, 1, 1]]  # 3x + 4y + u + v <= 120
salt_constant = [120]

bounds = [(0), (0)]  # x >= 0, y >= 0

c = np.zeros(4)

result = linprog(
    c,
    butter_coeff,
    butter_constant,
    flour_coeff,
    flour_constant,
    yeast_coeff,
    yeast_constant,
    salt_coeff,
    salt_constant,
    bounds,
)

print(result)
