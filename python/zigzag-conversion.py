def read_matrix(matrix):
    res = ''
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                continue
            res += matrix[i][j]
    return res

def convert(s: str, num_rows: int) -> str:
    if num_rows == 1 or len(s) == 1:
        return s

    matrix = [[0 for _ in range(len(s) // 2 + 1)] for _ in range(num_rows)] 
    
    s_counter = 0
    for x in range(len(s) // 2 + 1):
        for y in range(num_rows):
            if s_counter >= len(s):
                break
            if x == 0 or (y + x) % (num_rows - 1) == 0 or x % (num_rows - 1) == 0:
                matrix[y][x] = s[s_counter]
                s_counter += 1
            
    return read_matrix(matrix)

print(convert("PAYPALISHIRING", 3))
print(convert("PAYPALISHIRING", 4))
print(convert("PAYPALISHIRING", 1))
print(convert("PAYPALISHIRING", 2))
print(convert("PAYPALISHIRING", 5))
print(convert("ABCD", 2))
print(convert("ABCDE", 1))
print(convert("ABCDEF", 2))
print(convert("ABCDEFG", 3))
print(convert("ABCDEFGH", 4))
print(convert("ABCDEFGHI", 5))
print(convert("ABCDEFGHIJ", 3))
