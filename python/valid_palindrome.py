def valid_palindrome(s):
    new_str = ""

    for c in s:
        if c.isalnum():
            new_str += c.lower()

    return new_str == new_str[::-1]


s = "A man, a plan, a canal: Panama"
print(valid_palindrome(s))  # true

s = "race a car"
print(valid_palindrome(s))  # false
