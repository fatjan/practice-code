import math
def minOperationsToMakeMedianK(nums, k: int) -> int:
    nums.sort()
    n = len(nums)
    print(n)
    count = 0
    
    if n % 2 != 0:
        mid = n // 2 
        med = nums[mid]
        while med != k:
            if med < k:
                nums[mid] += 1
            else:
                nums[mid] -= 1
            nums.sort()
            count += 1
            mid = n // 2 
            med = nums[mid]
    else:
        mid = n // 2 - 1
        print(mid)
        med = math.ceil((nums[mid] + nums[mid+1]) / 2)
        print(med)
        while med != k:
            if med < k:
                nums[mid] += 1
            else:
                nums[mid] -= 1
            nums.sort()
            count += 1
            mid = n // 2 
            med = math.ceil((nums[mid] + nums[mid+1]) / 2)
    
    return count

print(minOperationsToMakeMedianK([1,2,3,4,5,6], 4)) # 0