def bulbSwitch(n):
    """
    There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.
    On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). 
    For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.
    Return the number of bulbs that are on after n rounds.
    >>> bulbSwitch(0)
    0
    >>> bulbSwitch(1)
    1
    >>> bulbSwitch(2)
    1
    >>> bulbSwitch(3)
    1
    >>> bulbSwitch(4)
    2
    >>> bulbSwitch(5)
    2
    >>> bulbSwitch(6)
    2
    >>> bulbSwitch(7)
    2
    >>> bulbSwitch(8)
    2
    >>> bulbSwitch(9)
    3
    >>> bulbSwitch(10)
    3
    >>> bulbSwitch(11)
    3
    >>> bulbSwitch(12)
    3
    >>> bulbSwitch(13)
    3
    >>> bulbSwitch(14)
    3
    >>> bulbSwitch(15)
    3
    >>> bulbSwitch(16)
    4
    >>> bulbSwitch(17)
    4
    >>> bulbSwitch(18)
    4
    >>> bulbSwitch(19)
    4
    >>> bulbSwitch(20)
    4
    >>> bulbSwitch(21)
    4
    >>> bulbSwitch(22)
    4
    >>> bulbSwitch(23)
    4
    >>> bulbSwitch(24)
    4
    >>> bulbSwitch(25)
    5
    >>> bulbSwitch(30)
    5
    >>> bulbSwitch(35)
    5
    >>> bulbSwitch(36)
    6      
    >>> bulbSwitch(40)
    6
    >>> bulbSwitch(49)
    7
    >>> bulbSwitch(50)
    7
    >>> bulbSwitch(60)
    7
    >>> bulbSwitch(70)
    8
    >>> bulbSwitch(80)
    8
    >>> bulbSwitch(81)
    9
    >>> bulbSwitch(90)
    9
    >>> bulbSwitch(99)
    9
    >>> bulbSwitch(100)
    10
    >>> bulbSwitch(120)
    10
    >>> bulbSwitch(121)
    11
    >>> bulbSwitch(1000)
    31
    >>> bulbSwitch(10000)
    100
    >>> bulbSwitch(100000)
    316
    >>> bulbSwitch(1000000)
    1000
    >>> bulbSwitch(10000000)
    3162
    >>> bulbSwitch(100000000)
    10000
    """
    if n == 0:
        return 0
    
    if n == 1 or n == 2:
        return 1

    bulbs = ["on"] * n
    count = n

    for time in range(2, n+1):
        repeat = n // time
        for i in range(repeat):
            index = time * (i + 1) - 1
            if bulbs[index] == "on":
                bulbs[index] = "off"
                count -= 1
            else:
                bulbs[index] = "on"
                count += 1

    return count

            
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)


