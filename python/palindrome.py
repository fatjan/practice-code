def is_palindrome(n):
    initial = ""
    n = str(n)

    for char in n:
        if not char.isalpha():
            continue
        initial += char.lower()

    return initial == initial[::-1]

print(is_palindrome("level"))
print(is_palindrome("levels"))
print(is_palindrome(12321))
print(is_palindrome(12345))
print(is_palindrome(123321))
print(is_palindrome(123456))
print(is_palindrome(1234567))
print(is_palindrome(12345678))
print(is_palindrome(123456789))
print(is_palindrome(1234567890))
print(is_palindrome(12345678901))
print(is_palindrome("A man, a plan, a canal: Panama"))