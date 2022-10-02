# What is the smallest value of n such that an algorithm
# whose running time is 100n2 runs faster than
# an algorithm whose running time is 2n on the same machine?

endless = 100

for n in range(1, endless):
    if 100 * n**2 < 2**n:
        print("100n^2", 100 * n**2)
        print("2 ^ n", 2**n)
        print("n", n)
        print()

# answer = 15
