def diagonalSum(mat) -> int:
        rows, cols = len(mat), len(mat[0])
        total = 0
        for i in range(rows):
            for j in range(cols):
                if i == j:
                    total += mat[i][j]
                if i + j + 1 == rows:
                    total += mat[i][j]
        
        return total


print(diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))
print(diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))
print(diagonalSum([[5]]))
print(diagonalSum([[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]]))
