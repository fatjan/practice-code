def is_convertible_to_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

result = []

def process_bit(n):
    bits = ['?'] * 32
    len_bits = len(bits) - 1
    for _ in range(n):
        line = input()
        command = line.strip().split()
        if len(command) < 2:
            return  # Skip invalid commands
            
        first_command = command[0]
        if first_command == 'SET':
            index = len_bits - int(command[1])
            bits[index] = '1'
        elif first_command == 'CLEAR':
            index = len_bits - int(command[1])
            bits[index] = '0'
        else:
            index1 = len_bits - int(command[1])
            index2 = len_bits - int(command[2])
            if bits[index1] == '?' or bits[index2] == '?':
                bits[index1] = '?'
                continue
            if first_command == 'OR':
                res = int(bits[index1]) | int(bits[index2])
            else:
                res = int(bits[index1]) & int(bits[index2])
            bits[index1] = str(res)

    result.append(('').join(bits))

user_input = input()
while user_input.strip() != '0':
    if is_convertible_to_int(user_input):
        n = int(user_input)
        process_bit(n)
    user_input = input()
    print('user_input: ', user_input)
    
for i in range(len(result)):
    print(result[i])
