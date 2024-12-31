def count_alternate_sub(nums):
    len_arr = len(nums)
    # def is_alternating(arr):
    #     len_arr = len(arr)
    #     if len_arr == 1:
    #         return True
    #     for k in range(1, len_arr):
    #         if arr[k] != arr[k-1]:
    #             continue
    #         else:
    #             return False
    #     return True
    
    count = 0
    # for i in range(len_arr):
    #     for j in range(i+1, len_arr+1):
    #         sub = nums[i:j]
    #         if is_alternating(sub):
    #             count += 1
    l, r = 0, 1
    while l < len_arr:
        while r < len_arr and nums[r] != nums[r-1]:
            r += 1
        count += (r-l)*(r-l+1)//2
        l = r
        r += 1
        
    return count

print(count_alternate_sub([1, 2, 3, 4, 5])) # 15
print(count_alternate_sub([1, 2, 1, 2, 1])) # 7
print(count_alternate_sub([0,1,1,1])) # 5