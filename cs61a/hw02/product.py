from operator import add, mul, pow


def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term:  a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
    print("n", n)
    print("term", term)

    result = 1
    for i in range(1, n + 1):
        if term == "identity":
            x = i
        elif term == "square":
            x = pow(i, 2)
        elif term == "increment":
            x = add(i, 1)
        elif term == "triple":
            x = mul(i, 3)

        result *= x

    # for i in range(1, n + 1):
    #     result *= term(i)

    return result
