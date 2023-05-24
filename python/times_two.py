def times_two(nums):
    result = []
    for num in nums:
        result.append(num * 2)
    return result

nums = [1, 2, 3, 4, 5]
print(times_two(nums))

nums = [1, 2, 3, 4, 5]
print([num * 2 for num in nums])