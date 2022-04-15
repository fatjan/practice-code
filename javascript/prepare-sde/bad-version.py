import random


def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    version = 2
    if n == 1:
        return n
    
    mid = (1 + n) // 2
    
    while (mid != 2):
        if mid + 1 == 2:
            return mid + 1
        mid = (mid + n) // 2

print(firstBadVersion(5))