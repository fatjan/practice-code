def sortedSquares(nums):
    squared = []
    
    for i in range(len(nums)):
        squared.append(nums[i]**2)

    squared.sort()
    return squared

print(sortedSquares([-4,-1,0,3,10]))