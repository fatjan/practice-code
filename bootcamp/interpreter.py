import sys

def math(words):
    result = 0
    for i in range(len(words)):
        if words[i] == '+':
            result += int(words[i+1])
        elif words[i] == '-':
            result -= int(words[i+1])
    return result

def interpret(words, labels):
    labels[words[0]] = words[1:]
    to_be_print = []
    for i in range(len(words[1:])):
        if words[i] == 'PRINT' or words[i] == 'PRINTLN':
            to_be_print = words[i+1:]
            break
        elif words[i] == 'PRINTLN':
            to_be_print = words[i+1:]
            to_be_print.append('\n')
            break
        elif words[i] == 'LET':
            variables[words[i+1]] = words[i+2]
        # elif words[i] == 'GOTO':
    
    return labels, ' '.join(to_be_print)

labels = {}
variables = {}

user_input = sys.stdin.readlines()

for line in user_input:
    line = line.rstrip('\n')
    words = line.split()
    labels, to_be_print = interpret(words, labels)
    print(to_be_print)