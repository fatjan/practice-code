def clearDigits(s: str) -> str:
    stack = []
    stack.append(s[0])
    
    for i in range(1, len(s)):
        if stack and s[i].isnumeric():
            stack.pop()
        if not s[i].isnumeric():
            stack.append(s[i])
    
    return "".join(stack)

print(clearDigits("a1b2c3")) # ""
print(clearDigits("abc")) # "abc"
print(clearDigits("cb34")) # ""
print(clearDigits("abc123rt")) # "rt"
print(clearDigits("a1b2c3d4e5f6g7h8i9j0")) # "abcdefghij"
print(clearDigits("a1b2c3d4e5f6g7h8i9j0k")) # "abcdefghijk"
print(clearDigits("a1b2c3d4e5f6g7h8i9j0k1")) # "abcdefghijk"
print(clearDigits("abiawue1234basjebj23bnaoia23naosh4asb2asoh24355a")) # "abibasjebjbnasbasohas"