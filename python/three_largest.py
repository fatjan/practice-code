def three_largest(nums):
    result = []
    for num in nums:
        if len(result) < 3:
            result.append(num)
        else:
            if num > min(result):
                result.remove(min(result))
                result.append(num)
    return sorted(result)


print(three_largest([1, 2, 3, 4, 5]))

def largest(nums):
    result = [float("-inf")] * 3

    for num in nums:
        if num > result[0]:
            result[0], result[1], result[2] = num, result[0], result[1]
        elif num > result[1]:
            result[1], result[2] = num, result[1]
        elif num > result[2]:
            result[2] = num
    return result

nums = [10, 4, 5, 2, 8, 6, 2, 3, 4, 5]
print(largest(nums))
            
    