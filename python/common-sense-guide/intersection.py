def find_intersection(arr1, arr2):
    if len(arr2) < len(arr1):
        arr1, arr2 = arr2, arr1
    
    keep_arr2 = {}
    for item in arr2:
        keep_arr2[item] = True
    
    intersection = []
    for item in arr1:
        if item in keep_arr2:
            intersection.append(item)
    
    return intersection

# Given two arrays
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

# Find the intersection of two arrays
intersection = find_intersection(arr1, arr2)
print("Intersection of two arrays:", intersection)

# This way, we can find the intersection of two arrays in Python, not using O(N*M) time complexity. But then using O(N) time complexity,
# however, the space complexity is O(N) as well.