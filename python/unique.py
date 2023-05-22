# Implement a Python function that takes a list of numbers as input and returns a new list that contains only the unique elements from the original list, preserving their original order.

# For example, given the list [1, 2, 3, 2, 4, 3, 5], the function should return [1, 2, 3, 4, 5] as the output.

def unique(nums):
    result = []
    for num in nums:
        if num not in result:
            result.append(num)
    return sorted(result)

nums = [1, 2, 3, 2, 4, 3, 5]
print(unique(nums))

nums = [1, 2, 3, 2, 4, 4, 1, 3, 5, 1, 2, 3, 4, 5, 6, 7, 8, 6, 5, 4, 3, 2, 1]
print(unique(nums))
