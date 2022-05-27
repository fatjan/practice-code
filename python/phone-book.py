import sys

lines = ['3', 'sam 99912222', 'tom 11122222', 'harry 12299933', 'sam', 'edward', 'harry']
# for line in sys.stdin:
#     lines.append(line)
    
n = int(lines[0])
map = {}
for i in range(1, len(lines)):
    if i <= n:
        data = lines[i].split()
        map[data[0]] = data[1]
    elif lines[i] in map:
        print(f'{lines[i]}={map[lines[i]]}')
    else:
        print('Not found')