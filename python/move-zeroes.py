def move_zeroes(nums):
    print(nums)
    non_zero_index = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1
    
    nums[non_zero_index:] = [0] * (len(nums) - non_zero_index)
    print(nums)
    print()

move_zeroes([0,1,0,3,12])
move_zeroes([0])
move_zeroes([1])
move_zeroes([1,0,1])
move_zeroes([1,0,0,1])