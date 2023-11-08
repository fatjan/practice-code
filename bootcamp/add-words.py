import sys

user_input = sys.stdin.readlines()

key_to_value = {}
value_to_key = {}

def add_to_def(key, value):
    value = int(value)
    if key in key_to_value:
        del value_to_key[key_to_value[key]]
    key_to_value[key] = value
    value_to_key[value] = key

def print_line(sentences):
    res_sentence = sentences[1] + ' '
    unknown = False

    if sentences[1] in key_to_value:
        result = int(key_to_value[sentences[1]])
    else:
        result = 0
        unknown = True
    
    for i in range(2, len(sentences)):
        if sentences[i] in ['-', '+']:
            res_sentence += sentences[i]
            if sentences[i+1] in key_to_value:
                num = int(key_to_value[sentences[i+1]])
                if sentences[i] == '-':
                    result -= num
                elif sentences[i] == '+':
                    result += num
            else:
                unknown = True
        else:
            res_sentence += sentences[i]
            
        res_sentence += ' '
    
    if result in value_to_key and not unknown:
        res_sentence += value_to_key[result]
    else:
        res_sentence += 'unknown'
    print(res_sentence)

for i in range(len(user_input)):
    user_input[i] = user_input[i].rstrip('\n')
    sentences = user_input[i].split()
    if sentences[0] == 'def':
        add_to_def(sentences[1], sentences[2])
    elif sentences[0] == 'calc':
        print_line(sentences)
    else:
        key_to_value = {}
        value_to_key = {}