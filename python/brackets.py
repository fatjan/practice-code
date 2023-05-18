def solution(S):
    # Implement your solution here
    cl = '}])'
    if S[0] in cl:
        return 0
    
    stack = []
    op = '{[('

    keep = {
        '{': '}',
        '(': ')',
        '[': ']',
    }

    for br in S:
        if br in op:
            stack.append(br)
        elif br == keep[stack[-1]]:
            stack.pop()

    if len(stack) == 0:
        return 1
    
    return 0

solution('{[()()]}')
# 1

solution('([)()]')
# 0