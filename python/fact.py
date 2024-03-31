def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) # 120
print(factorial(6)) # 720
print(factorial(7)) # 5040
print(factorial(3)) # 6
print(factorial(1)) # 1
print(factorial(10)) # 3628800
print(factorial(11)) # 39916800
print(factorial(12)) # 479001600
print(factorial(15)) # 1307674368000
print(factorial(20)) # 2432902008176640000
print(factorial(30)) # 265252859812191058636308480000000
print(factorial(50)) # 30414093201713378043612608166064768844377641568960512000000000000