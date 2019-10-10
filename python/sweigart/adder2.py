import doctest

def addTwoNumbers(a, b):
    '''
    Returns the sum of a and b.

    >>> addTwoNumbers(2, 2)
    4
    >>> addTwoNumbers(2, 4)
    6
    '''
    return a + b

doctest.testmod()
