def getSmallestString(n: int, k: int) -> str:
        alfa = 'abcdefghijklmnopqrstuvwxyz'
        last = len(alfa)
        res = ''
        for i in range(n):
            while k - last < n - (i+1):
                last -= 1
            res += alfa[last-1]
            k -= last

        return res[::-1]

print(getSmallestString(3, 27))
print(getSmallestString(5, 73))
print(getSmallestString(5, 130))
print(getSmallestString(5, 10))
print(getSmallestString(5, 26))
print(getSmallestString(5, 52))