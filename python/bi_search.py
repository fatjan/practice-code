from attr import Factory
from sqlalchemy import false


def binary_search_recursive(arr, num, left, right):
    if left > right:
        return False

    mid = left + (right - left) // 2

    if arr[mid] == num:
        return True
    elif num < arr[mid]:
        return binary_search_recursive(arr, num, left, mid - 1)
    else:
        return binary_search_recursive(arr, num, mid + 1, right)


arr = [1, 5, 9, 54, 74, 62, 115]
print(binary_search_recursive(arr, 62, 0, len(arr) - 1))  # True
print(binary_search_recursive(arr, 162, 0, len(arr) - 1))  # False


def binary_search_iterative(arr, num):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == num:
            return True
        elif num < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return False


arr = [1, 5, 9, 54, 74, 62, 115]
print(binary_search_iterative(arr, 62))  # True
print(binary_search_iterative(arr, 162))  # False
