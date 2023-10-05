from collections import Counter

def frequencySort(s):
    # Count the frequency of each character in the string
    char_count = Counter(s)
    
    # Sort the characters by their frequency in decreasing order
    sorted_chars = sorted(char_count, key=lambda x: char_count[x], reverse=True)
    
    # Build the sorted string
    sorted_string = ''.join([char * char_count[char] for char in sorted_chars])
    
    return sorted_string

print(frequencySort('tree'))
print(frequencySort('cccaaa'))
print(frequencySort('Aabb'))
print(frequencySort(''))
print(frequencySort('a'))
print(frequencySort('aabewjkwejkwiujkasgbweralwehr'))