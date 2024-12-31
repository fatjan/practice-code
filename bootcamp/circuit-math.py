import sys

user_input = sys.stdin.readlines()

n = user_input[0].strip()
n = int(n)

values = user_input[1].strip().split()
for i in range(len(values)):
    if values[i] == 'T':
        values[i] = True
    elif values[i] == 'F':
        values[i] = False

circuits = user_input[2].strip().split()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

operations = "*+-"

def calc(a, b, operation):
    a = values[alphabet.index(a)]
    b = values[alphabet.index(b)]
    if operation == '*':
        result = a and b
    elif operation == '+':
        result = a or b
    
    return 'T' if result else 'F'

res = []
index = 2
while index < len(circuits):
    if circuits[index] == '*' or circuits[index] == '+':
        a = circuits[index-2]
        b = circuits[index-1]
        op = circuits[index]
        calc_result = calc(a, b, op)
        res.append(calc_result)

    elif circuits[index] == '-':
        a = circuits[index-1]
        a = values[alphabet.index(a)]
        calc_result = not a
        res.append('T' if calc_result else 'F')
    
    index += 1

print('circuits: ', circuits)