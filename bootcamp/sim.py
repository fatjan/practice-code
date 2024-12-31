def simulate_typing(input_str):
    text_buffer = []
    cursor_position = 0

    for char in input_str:
        if char == '<':
            cursor_position = max(cursor_position - 1, 0)
        elif char == '[':
            cursor_position = 0
        elif char == ']':
            cursor_position = len(text_buffer)
        else:
            # Insert the character at the cursor position
            text_buffer.insert(cursor_position, char)
            cursor_position += 1

    return ''.join(text_buffer)

# Read the number of test cases
num_test_cases = int(input())

for _ in range(num_test_cases):
    # Read each test case
    test_case = input().strip()
    
    # Simulate typing and print the result
    result = simulate_typing(test_case)
    print(result)
