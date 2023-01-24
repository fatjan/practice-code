from scipy.optimize import linprog

# Set up values relating to both minimum and maximum values of y
coefficients_inequalities = [[-1, -1]]  # require -1*x + -1*y <= -180
constants_inequalities = [-180]
coefficients_equalities = [[3, 12]]  # require 3*x + 12*y = 1000
constants_equalities = [1000]
bounds_x = (30, 160)  # require 30 <= x <= 160
bounds_y = (10, 60)  # require 10 <= y <= 60

# Find and print the minimal value of y
coefficients_min_y = [0, 1]  # minimize 0*x + 1*y
res = linprog(
    coefficients_min_y,
    A_ub=coefficients_inequalities,
    b_ub=constants_inequalities,
    A_eq=coefficients_equalities,
    b_eq=constants_equalities,
    bounds=(bounds_x, bounds_y),
)
print("Minimum value of y =", res.fun)

# Find and print the maximal value of y = minimal value of -y
coefficients_max_y = [0, -1]  # minimize 0*x + -1*y
res = linprog(
    coefficients_max_y,
    A_ub=coefficients_inequalities,
    b_ub=constants_inequalities,
    A_eq=coefficients_equalities,
    b_eq=constants_equalities,
    bounds=(bounds_x, bounds_y),
)
print("Maximum value of y =", -res.fun)  # opposite of value of -y
