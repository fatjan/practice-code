def majorityElement(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    # Second pass to verify the candidate
    count = 0
    for num in nums:
        if num == candidate:
            count += 1

    if count > len(nums) // 2:
        return candidate
    else:
        return -1  # There is no majority element

print(majorityElement([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5]))
print(majorityElement([1, 2, 3, 4, 5, 5, 5, 5, 5, 5]))
print(majorityElement([1, 2, 3, 4, 5, 5, 5, 5, 5]))
print(majorityElement([1, 2, 3, 4, 5, 5, 5, 5]))
print(majorityElement([1, 2, 3, 4, 5, 5, 5]))
print(majorityElement([1, 2, 3, 4, 5, 5]))
print(majorityElement([1, 2, 3, 4, 5]))
print(majorityElement([1, 2, 3, 4]))