import sys

def dictionary(words, key_value, value_key):
    key_value[words[1]] = int(words[2])
    value_key[int(words[2])] = words[1]
    return key_value, value_key

def create_line(words, key_value, value_key):
    result = 0
    res_unknown = False

    line = ''
    for i in range(1, len(words)):
        if words[i] in key_value:
            if words[i - 1] == '+' or words[i - 1] == 'calc':
                result += key_value[words[i]]
            elif words[i - 1] == '-':
                result -= key_value[words[i]]
        elif words[i] != '=' and words[i] != '+' and words[i] != '-':
            res_unknown = True
        line += words[i] + ' '

    if not res_unknown:
        if result in value_key:
            line += value_key[result]
        else:
            line += 'unknown'
    else:
        line += 'unknown'

    return line, key_value, value_key

key_value = {}
value_key = {}
    
def convert(words, key_value, value_key):
    if words[0] == 'def':
        key_value, value_key = dictionary(words, key_value, value_key)
    elif words[0] == 'calc':
        line, key_value, value_key = create_line(words, key_value, value_key)
        print(line)
    else:
        key_value = {}
        value_key = {}
    
    return key_value, value_key


user_input = sys.stdin.readlines()
for i in range(len(user_input)):
    user_input[i] = user_input[i].rstrip('\n')
    words = user_input[i].split()
    key_value, value_key = convert(words, key_value, value_key)