from typing import List
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    keep = {}

    def find_duplicate(indexes, index):
        for i in indexes:
            if abs(i - index) <= k:
                return True

        return False

    for i in range(len(nums)):
        if nums[i] not in keep:
            keep[nums[i]] = [i]
        else:
            indexes = keep[nums[i]]
            found = find_duplicate(indexes, i)
            if found:
                return True
            keep[nums[i]].append(i)
    
    return False

print(containsNearbyDuplicate([1,2,3,1,2,3], 2))
print(containsNearbyDuplicate([1,0,1,1], 1))
print(containsNearbyDuplicate([1,2,3,1], 3))
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))