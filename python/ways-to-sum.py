# please improve the following function
# it should return the number of ways to sum k numbers to total
# for example, ways_to_sum(4, 2) should return 3
# because there are 3 ways to sum 2 numbers to 4:
# 1 + 3
# 2 + 2
# 3 + 1
# def ways_to_sum(total, k):
#     if total == 0 and k == 0:
#         return 1
#     if total <= 0 or k <= 0:
#         return 0
#     return ways_to_sum(total - 1, k - 1) + ways_to_sum(total - 2, k - 1) + ways_to_sum(total - 3, k - 1)
def ways_to_sum(total, k):
    if total == 0 and k == 0:
        return 1
    if total <= 0 or k <= 0:
        return 0
    return ways_to_sum(total - 1, k - 1) + ways_to_sum(total - 2, k - 1) + ways_to_sum(total - 3, k - 1)

# print(ways_to_sum(4, 2))
# print(ways_to_sum(5, 3))
print(ways_to_sum(4, 2))
print(ways_to_sum(3, 2))
print(ways_to_sum(2, 2))

# print(ways_to_sum(6, 4))
# print(ways_to_sum(7, 5))

# write a function to convert 0 to a, b to 1, c to 2, etc.
def convert_to_number(s):
    result = 0
    for i in range(len(s)):
        result = result * 26 + ord(s[i]) - ord('a')
    return result

# write a function that is a reverse of the previous one
def convert_to_string(n):
    result = ''
    while n > 0:
        result = chr(ord('a') + n % 26) + result
        n //= 26
    return result


def minimumGroups(predators):
    # Write your code here
    groups = []
    for i in range(len(predators)):
        if predators[i] == -1:
            groups.append([i])
        else:
            for group in groups:
                if predators[i] in group:
                    group.append(i)
                    break
    return len(groups)

# print(minimumGroups([-1, 8, 6, 0, 7, 3, 8, 9, -1, 6]))
# print(minimumGroups([-1, 0, 1]))