def cumulative_sum_dp_version(arr):
    """
        >>> cumulative_sum_dp_version([4, 6, 1, 3, 1, 5])
        [20, 16, 10, 9, 6, 5]
        >>> cumulative_sum_dp_version([1, 2, 3, 4, 5])
        [15, 14, 12, 9, 5]
    """
    cum_sum = [0] * len(arr)
    cum_sum[-1] = arr[-1]
    for i in range(len(arr) - 2, -1, -1):
        cum_sum[i] = cum_sum[i+1] + arr[i]
    return cum_sum

def cumulative_sum_in_place(arr):
    """
        >>> cumulative_sum_in_place([4, 6, 1, 3, 1, 5])
        [20, 16, 10, 9, 6, 5]
        >>> cumulative_sum_in_place([1, 2, 3, 4, 5])
        [15, 14, 12, 9, 5]
    """
    for i in range(len(arr) - 2, -1, -1):
        arr[i] = arr[i+1] + arr[i]
    return arr

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
