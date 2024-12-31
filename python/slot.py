def solution(A, B, S):
    # Implement your solution here
    if len(A) > S:
        return False
    
    stack = []
    result = []

    def process_to_result(item, stack, result):
        index = stack.index(item)
        take = stack.pop(index)
        if take in result:
            return False
        result.append(take)

    for i in range(len(A)):
        slot = A[i]
        room = B[i]
        if slot not in stack:
            stack.append(slot)
        else:
            process_to_result(slot, stack, result)
        
        if room not in stack:
            stack.append(room)
        else:
            process_to_result(room, stack, result)

    for num in stack:
        if num not in result:
            result.append(num)
            if len(result) == len(A):
                break

    if len(result) == len(A):
        return True
    
    return False

print(solution([1, 2, 1, 6, 8, 7, 8], [2, 3, 4, 7, 7, 8, 7], 10))