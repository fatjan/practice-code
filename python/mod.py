def f(a, b):
    return a % b

result = 0
for i in range(10):
    if f(i, 2) == 0:
        result += i
    else:
        result -= i

print(result)

for i in range(3):
    for j in range(i, 3):
        j -= i
    print(j)