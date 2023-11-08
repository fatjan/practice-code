import sys

user_input = sys.stdin.readlines()

def convert(line):
    keyboard = '1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./'
    for i in line:
        if i == ' ' or i == '\n':
            print(i, end='')
        else:
            print(keyboard[keyboard.index(i)-1], end='')
    print()

for line in user_input:
    convert(line)