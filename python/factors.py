import math

def kthFactor(n, k):
    factors = []

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            print('n', n)
            print('n // i', n // i)
            if i != n // i:
                factors.append(n // i)
    
    if k > len(factors):
        return -1
    
    return sorted(factors)[k - 1]

print(kthFactor(12, 3))
print(kthFactor(7, 2))
print(kthFactor(4, 4))