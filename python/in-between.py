import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def getTotalX(a, b):
    """
    >>> getTotalX([2, 4], [16, 32, 96])
    3
    >>> getTotalX([2, 6], [24, 36])
    2
    >>> getTotalX([3, 4], [24, 48])
    2
    """
    for i in range(len(a) - 1):
        a[i + 1] = lcm(a[i], a[i + 1])
    for i in range(len(b) - 1):
        b[i + 1] = math.gcd(b[i], b[i + 1])
    print(a)
    print(b)

    result = 0
    for i in range(a[-1], b[0] + 1, a[-1]):
        if all([x % i == 0 for x in b]):
            result += 1
    return result

    # while num <= b[0]:
    #     is_a_ok = True
    #     for num_in_a in a:
    #         if num % num_in_a != 0:
    #             is_a_ok = False
    #             break
        
    #     is_b_ok = True
    #     for num_in_b in b:
    #         if num_in_b % num != 0:
    #             is_b_ok = False
    #             break
        
    #     if is_a_ok and is_b_ok:
    #         result.append(num)
    #     num += num

    return len(result)

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=True)
print(getTotalX([2, 4], [16, 32, 96])) # 3
print(getTotalX([2, 6], [24, 36])) # 2
print(getTotalX([3, 4], [24, 48])) # 2