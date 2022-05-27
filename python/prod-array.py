def productExceptSelf(nums):
    res = []
    prefix = []
    postfix = []

    for i in range(len(nums)):
        print(i)
        if i == 0:
            prefix.append(nums[i])
        else:
            prefix.append(nums[i] * prefix[i - 1])


print(productExceptSelf([1, 2, 3, 4]))
