import sys

n = int(sys.stdin.readline())

def find_conformity(n):
    combinations = {}
    max_value = 0

    for _ in range(n):
        choices = tuple(sorted(map(int, sys.stdin.readline().split())))
        if choices in combinations:
            combinations[choices] += 1
        else:
            combinations[choices] = 1
        max_value = max(max_value, combinations[choices])

    result = 0
    for key, value in combinations.items():
        if value == max_value:
            result += value

    return result

print(find_conformity(n), end='')
