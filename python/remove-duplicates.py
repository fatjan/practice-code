class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        
        print(A)
        write_index = 1  # Start from the second element
        for i in range(1, len(A)):
            if A[i] != A[i - 1]:
                A[write_index] = A[i]
                write_index += 1
        
        print(A)
        print(write_index)
        # Truncate the list to the new length
        while len(A) > write_index:
            A.pop()
        
        return len(A)
            
solution = Solution()

print(solution.removeDuplicates([1, 1, 2])) # 2
print(solution.removeDuplicates([1, 1, 2, 3, 3])) # 3
print(solution.removeDuplicates([1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 8, 9, 9, 10])) # 10
print(solution.removeDuplicates([1, 1, 1, 1, 1])) # 1
print(solution.removeDuplicates([1, 2, 3])) # 3