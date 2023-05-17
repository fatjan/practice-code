# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def solution(N):
    # Implement your solution here
    binary = decimal_to_binary(N)
    digit = str(binary)
    print(digit)
    longest = 0
    counter = 0
    for i in range(0, len(digit)):
        if digit[i] == '1':
            for j in range(i + 1, len(digit)):
                if digit[j] == '0':
                    counter += 1
                else:
                    print('string', digit[i:j])
                    longest = max(longest, counter)
                    print('counter: ', counter)
                    print('longest: ', longest)
                    counter = 0
                    print('')
                    i += 2
    
    return longest

longest = solution(1376796946)
print(longest)