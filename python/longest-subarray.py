def longestSubarray(arr):
    left, right = 0, 0
    window_counts = {}
    max_length = 0
    max_subarray_start = 0

    while right < len(arr):
        # Add current number to window_counts
        if arr[right] not in window_counts:
            window_counts[arr[right]] = 0
        window_counts[arr[right]] += 1

        # Check if there are more than 2 distinct numbers in the current window
        while len(window_counts) > 2:
            window_counts[arr[left]] -= 1
            if window_counts[arr[left]] == 0:
                del window_counts[arr[left]]
            left += 1

        # Update the result if needed
        if right - left + 1 > max_length:
            max_length = right - left + 1
            max_subarray_start = left

        right += 1

    return arr[max_subarray_start:max_subarray_start + max_length]

print(longestSubarray([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
print(longestSubarray([1, 1, 2]))