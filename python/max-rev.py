from sympy import symbols, Eq, solve

x, y, u, v = symbols("x y u v")

butter = Eq(x + y + 5 * u + 3 * v, 50)

flour = Eq(2 * x + 2 * y + u + v, 130)

yeast = Eq(x + y + u + 4 * v, 70)

salt = Eq(3 * x + 4 * y + u + v, 120)

print(solve((butter, flour, yeast, salt), (x, y, u, v)))
