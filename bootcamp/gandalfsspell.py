import sys
 
lines = []
for _ in range(2):
    lines.append(sys.stdin.readline().rstrip('\n'))
    
map = lines[0]
sentences = lines[1].split()

def is_valid(map, sentences):
    if len(map) != len(sentences):
        return False

    keep = {}
    values = []
    for i in range(len(map)):
        if map[i] not in keep:
            if sentences[i] in values:
                return False
            keep[map[i]] = sentences[i]
            values.append(sentences[i])
        elif keep[map[i]] != sentences[i]:
            return False

    return True

print(is_valid(map, sentences))