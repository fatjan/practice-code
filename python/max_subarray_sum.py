def max_subarray_sum(nums):
    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

nums = [1, -2, 3, 4, -1, 2, 1, -5, 4]
max_sum = max_subarray_sum(nums)
print(max_sum)