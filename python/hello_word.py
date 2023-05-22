# Write a Python function that takes a string as input and returns the count of each character in the string. The function should ignore spaces and treat uppercase and lowercase characters as the same.

# For example, given the string "Hello World", the function should return a dictionary with the following key-value pairs: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}.

# Please take a moment to think about the problem and come up with a solution. Once you're ready, explain your approach and provide the Python code to solve the problem.

def hello(string):
    s = string.lower()
    d = {}
    for c in s:
        if c.isalpha():
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
    return d
            
print(hello("Hello World"))
print(hello("Hello World! aku23*23n kawejrhk"))
