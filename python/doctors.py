def solution(A, B, S):
    # Implement your solution here
    if len(A) > S:
        return False
    
    stack = []
    result = []
    for i in range(len(A)):
        slot = A[i]
        room = B[i]
        if slot not in stack:
            stack.append(slot)
        else:
            index = stack.index(slot)
            take = stack.pop(index)
            if take in result:
                return False
            result.append(take)
        

        if room not in stack:
            stack.append(room)
        else:
            index = stack.index(room)
            take = stack.pop(index)
            if take in result:
                return False
            result.append(take)
    
    for num in stack:
        if num not in result:
            result.append(num)
            if len(result) == len(A):
                break
    if len(result) == len(A):
        return True
    
    return False

# print(solution([1, 1, 3], [2, 2, 1], 3))
# print(solution([1, 2, 4, 3], [1, 3, 2, 3], 3))
# print(solution([2, 5, 6, 5], [5, 4, 2, 2], 8))
# print(solution([1, 2, 1, 6, 8, 7, 8], [2, 3, 4, 7, 7, 8, 7], 10))
print(solution([1, 2, 1, 6, 8, 7, 8], [2, 3, 4, 7, 7, 8, 7], 10))
