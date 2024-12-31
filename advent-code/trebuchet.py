def read_input():
    """Read input from .txt file"""
    with open("input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

data = read_input()

def create_digits(word):
    """Find the digit in the word"""
    len_word = len(word)
    l = 0
    r = len_word - 1
    first_digit = None
    second_digit = None
    while first_digit is None or second_digit is None:
        if word[l].isdigit() and first_digit is None:
            first_digit = word[l]
        if word[r].isdigit() and second_digit is None:
            second_digit = word[r]
        if first_digit and second_digit:
            return int(first_digit + second_digit)
        l += 1
        r -= 1
  
    if first_digit:
        return int(first_digit * 2)
    elif second_digit:
        return int(second_digit * 2)

total = 0
for word in data:
    print(word)
    digits = create_digits(word)
    print(digits)
    total += digits
    print("")

print(total)