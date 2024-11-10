# Write a function that accepts an array of strings and returns the first duplicate value it finds. 
# For example, if the array is ["a", "b", "c", "d", "c", "e", "f"], the function should return "c", 
# since it’s duplicated within the array. (You can assume that there’s one pair of duplicates within the array.) 
# Make sure the function has an efficiency of O(N).

# The function should return the first duplicate value it finds in the array.
def find_first_duplicate(arr):
    seen = {}
    for char in arr:
        if char in seen:
            return char
        seen[char] = True
    return None

# Given an array of strings
arr = ["a", "b", "c", "d", "c", "e", "f"]

# Find the first duplicate value in the array
first_duplicate = find_first_duplicate(arr)
print("The array: ", arr)
print("First duplicate value in the array:", first_duplicate)

