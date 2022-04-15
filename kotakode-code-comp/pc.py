def hurufBergantian(inputString):
    output = 0
    for i in range(len(inputString)):
        if (inputString[i] == inputString[i-1] and i != 0):
            output += 1       
    return output

pcp = 'PCPCCPC'
pcp2 = 'PPCPPC'
pcp3 = 'PCPPCPPP'

print(hurufBergantian(pcp))
print(hurufBergantian(pcp2))
print(hurufBergantian(pcp3))
