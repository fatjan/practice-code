def power(n):
    for i in range(1, n+1):
        print('i: ', i)
        print('(2**m)%17 ', (2**i)%17)
        print('(-2**m)%17 ', (-2**i)%17)
        print(' ')

power(10)