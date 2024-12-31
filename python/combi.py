arr = [1,2,3,4,5]
n = len(arr)
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            print(arr[i],arr[j],arr[k])

l, m, r = 0, 1, 2
print()
while r < n:
    if m < r - 1:
        m += 1
    elif r < n - 1:
        r += 1
    else:
        l += 1
        m = l + 1
        r = m + 1