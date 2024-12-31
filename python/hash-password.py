def hash_password(password):
    """
    >>> hash_password("000A")
    108738449
    >>> hash_password("000B")
    108738450
    >>> hash_password("000C")
    108738451
    """

    n = len(password) - 1
    hash_value = 0
    for char in password:
        hash_value += ord(char) * (131 ** n)
        n -= 1
    return hash_value % (10**9 + 7)

def prefix_hash(password):
    """
    >>> prefix_hash("000A")
    14244736819
    """
    n = len(password)
    hash_value = 0
    for char in password:
        hash_value += ord(char) * 131 ** n
        n -= 1
    return hash_value

def authEvents(events):
    """
    >>> authEvents([["setPassword", "000A"], ["authorize", 108738450], ["authorize", 108738449], ["authorize", 244736787]])
    [0, 1, 1]
    >>> authEvents([["setPassword", "cAr1"], ["authorize", 223691457], ["authorize", 303580761], ["authorize", 100], ["setPassword", "d"], ["authorize", 100]])
    [1, 1, 0, 1]
    """
    password = ""
    res = []
    for event_item in events:
        [event, param] = event_item
        if event == "setPassword":
            hash_value = hash_password(param)
            password = param
        elif param == hash_value:
            res.append(1)
        else:
            prefix = prefix_hash(password)
            found = False
            for i in range(127):
                if (prefix + i) % (10**9 + 7) == param:
                    res.append(1)
                    found = True
                    break
            if not found:
                res.append(0)
    return res

res = authEvents([["setPassword", "000A"], ["authorize", 108738450], ["authorize", 108738449], ["authorize", 244736787]]) # [1, 0, 1]
print(res)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
