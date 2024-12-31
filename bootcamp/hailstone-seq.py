def find_result(num):
    if num % 2 == 0:
        return num // 2
    else:
        return num * 3 + 1


n = int(input())
total = n

def hailstone(n):
    global total
    if n == 1:
        return total
    
    res = find_result(n)
    total += res
        
    return hailstone(res)

hailstone(n)

print(total)