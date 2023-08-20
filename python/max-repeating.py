def max_repeating(sequence, word):
    l = 0
    r = 0
    substring = ''
    res = 0
    while r < len(sequence):
        part = sequence[l:r+1]
        if substring + part in sequence and part == word:
            res += 1
            substring += part
            l += len(word)
        elif len(part) == len(word):
            l += 1
        r += 1
    
    return res

print(max_repeating('ababab', 'ab'))
print(max_repeating('ababc', 'ba'))