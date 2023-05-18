def solution(S):
    # Implement your solution here
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