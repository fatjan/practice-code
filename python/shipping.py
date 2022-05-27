
def shipping(N, h):
  # Your solution starts here.
    result = []
    for i in range(N):
        compare = []
        for j in range(N):
            cost = h[j]
            if i == j:
                fee = 0
            else:
                fee = abs(j-i)
            compare.append(cost+fee)
        result.append(min(compare))
    return result

print(shipping(4, [1, 4, 2, 4]))