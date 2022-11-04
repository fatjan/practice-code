def removeKdigits(num, k):
    if k == len(num):
        return str(0)

    result = float("inf")

    for i in range(len(num) - k):
        rest = num[: i + 1] + num[i + 1 + k :]
        print(rest)
        result = min(result, int(rest))

    return str(result)


print(removeKdigits("112", 1))
