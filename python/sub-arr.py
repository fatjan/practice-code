def subArraySum(arr, n, s): 
    sums = [0] * n
    sums[0] = arr[0]
    for i in range(1, n):
        sums[i] = sums[i-1] + arr[i]

    l, r = 0, 0
    while l < n:
        if l == 0:
            if sums[r] == s:
                return [l+1, r+1]
        else:
            if sums[r] - sums[l-1] == s:
                return [l+1, r+1]
        r += 1
        if r == n:
            l += 1
            r = l
    return [-1]

print(subArraySum([1,2,3,7,5], 5, 12)) # [2, 4]
print(subArraySum([1,2,3,4,5,6,7,8,9,10], 10, 15)) # [1, 5]
print(subArraySum([1,2,3,4,5,6,7,8,9,10], 10, 55)) # [1, 10]
print(subArraySum([1,2,3,4,5,6,7,8,9,10], 10, 5)) # [1, 2]
print(subArraySum([1,2,3,4,5,6,7,8,9,10], 10, 10)) # [1, 3]
print(subArraySum([1,2,3,4,5,6,7,8,9,10], 10, 20)) # [1, 6]
print(subArraySum([1,2,3,4,5,6,7,8,9,10], 10, 30)) # [1, 7]
print(subArraySum([1,2,3,4,5,6,7,8,9,10], 10, 41)) # -1