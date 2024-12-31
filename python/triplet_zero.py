# def findTriplets(arr, n):
#     if n <= 2:
#         return 0
    
#     l, r = 0, 2
#     while l < n-2:
#         sub = arr[l:r+1]
#         print('sub:', sub)
#         if sum(sub) == 0:
#             return 1
#         r += 1
#         if r == n:
#             l += 1
#             r = l + 2
        
#     return 0

# print(findTriplets([-1, 0, 1, 2, -1, -4], 6)) # 1
# print(findTriplets([0, 0, 0], 3)) # 1
# print(findTriplets([0, 0], 2)) # 0
# print(findTriplets([0], 1)) # 0
# print(findTriplets([0, -1, 2, -3, 1], 5)) # 0
# print(findTriplets([97, -27, 2, -34, 61, -39], 6)) # 1

def findTriplets(self, arr, n):
        if n <= 2:
            return 0
        
        found = 0
        
        dp = [0] * n
        
        dp[0] = arr[0]
        dp[1] = arr[1] + dp[0]
        
        for i in range(2, n):
            dp[i] = arr[i] + dp[i-1]
        
        print(dp)
        
        return found

print(findTriplets([-1, 0, 1, 2, -1, -4], 6)) # 1