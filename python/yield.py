def all_pairs(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            yield arr[i], arr[j]

print(list(all_pairs([1, 2, 3, 4, 5])))