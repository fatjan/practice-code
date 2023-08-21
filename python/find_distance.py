def find_distance_value(arr1, arr2, d):
    res = 0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if abs(arr2[j] - arr1[i]) <= d:
                res += 1
                break
    return len(arr1) - res

print(find_distance_value([4,5,8], [10,9,1,8], 2))