# write requirements first before starting to code 
# ask data type, how many parameters, expected output
# edge cases, discuss from the beginning
# abt 5 minutes for discussing the requirements
# make interaction with the interviewer, does it look ok? etc.
# naming variable, as clear as possible, read more on Clean Code
# 1 liner is ok, but be careful for hidden complexity

def multiply(a, b):
    if a == 0 or b == 0:
        return 0

    if abs(a) > abs(b):
        a, b = b, a
        
    result = 0
    for _ in range(abs(a)):
        result += abs(b)
    
    should_return_negative = (a < 0 and b > 0) or (a > 0 and b < 0)
    
    if should_return_negative:
        return -result
    
    return result

print(multiply(2, 3))
print(multiply(-4, -5))
print(multiply(-21, 3))
print(multiply(14, -3))
print(multiply(1, 0))

def mod(a, b):
    if b == 0:
        return None 

    if b == 1:
        return 0

    if a < b:
        return a

    res = a
    while res >= b:
        res -= b
    
    return res

print(mod(9, 4)) 
print(mod(7, 4)) 
print(mod(17, 7)) 
print(mod(18, 9)) 




    
    

