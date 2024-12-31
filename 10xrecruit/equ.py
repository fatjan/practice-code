from scipy.optimize import minimize
import numpy as np

# Define the objective function to minimize
def objective_function(vars):
    x, y = vars
    return 3*x**2 + 3*y**2 - 1000*x - 1400*y + 185000

# Initial guess for x and y
initial_guess = [0, 0]

# Define bounds for x and y, if necessary
bounds = ((-np.inf, np.inf), (-np.inf, np.inf))

# Use an optimization method to find the minimum of the objective function
result = minimize(objective_function, initial_guess, bounds=bounds)

# Extract the optimal values of x and y
x_optimal, y_optimal = result.x

# Print the results
print("Optimal x:", x_optimal)
print("Optimal y:", y_optimal)
