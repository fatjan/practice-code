def evaluate_circuit(inputs, circuit_description):
    stack = []

    for char in circuit_description:
        if char.isalpha():
            # If the character is a variable, push its truth value onto the stack
            stack.append(inputs[char])
        elif char == '*':
            # AND operation
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operand1 and operand2
            stack.append(result)
        elif char == '+':
            # OR operation
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operand1 or operand2
            stack.append(result)
        elif char == '-':
            # NOT operation
            operand = stack.pop()
            result = not operand
            stack.append(result)

    # The final result is on top of the stack
    return stack[0]

# Read input
num_variables = int(input())
input_values = input().split()
inputs = {chr(ord('A') + i): input_values[i] == 'T' for i in range(num_variables)}
circuit_description = input().strip()

# Evaluate the circuit and print the result
result = evaluate_circuit(inputs, circuit_description)
print('T' if result else 'F')
