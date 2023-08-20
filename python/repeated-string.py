def repeatedString(s, n):
    # Write your code here
    count_a = s.count('a')
    div = n // len(s)
    mod = n % len(s)
    res = div * count_a + s[:mod].count('a')
    return res

print(repeatedString('aba', 10))