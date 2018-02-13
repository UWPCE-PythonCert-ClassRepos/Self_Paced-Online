'''
Thomas Horn
The following definitions are used to computer the Fibonacci and Lucas Series
throughout this program.
    Fibonacci - starts with 0, 1 and sums the previous 2 numbers
    Lucas - starts with 1, 2 and sums the previous 2 numbers
'''

def fibonacci(n):
    """ Returns the nth value in the fibonacci sequence. """
    if n <= 1:
        return 0
    else:
        first, second = 0, 1
        while n > 0:
            # first becomes the second number, and the second both nums added.
            first, second = second, (first+second)
            n -= 1
        return first


def lucas(n):
    """ Returns the nth value in the lucas sequence.   Identical to fibonacci
    except for different starting values. 
    """
    if n < 1:
        return 0
    else:
        # This seems backwards but seems to works in this order.
        first, second = 2, 1
        while n > 0:
            first, second = second, (first+second)
            n -= 1
        return first


def sum_series(n, first=0, second=1):
    """ sum_series defaults to the fibonacci sequence if only n is assigned a 
    parameter.  
        If first and second are given values, they will produce the nth value
    in a similar fashion to the lucas series beginning with the two optional
    parameters.
    """
    if n < 1:
        return 0
    else:
        while n > 0:
            first, second = second, (first+second)
            n -= 1
        return first


if __name__ == "__main__":
    # Test of fibonacci values. 
    print("Fibonacci: ")
    # Correct value.
    try:
        assert (fibonacci(10) ==  55)
    except AssertionError:
        print("Incorrect value.")
    # Incorrect value.
    try:
        assert (fibonacci(8) ==  55)
    except AssertionError:
        print("Incorrect value.")

    # Test of lucas values.
    print("Lucas: ")
    # Correct values.
    assert (lucas(7) == 29)
    assert (lucas(10) == 123)
    # Incorrect value.
    try: 
        assert (lucas(10) == 29)
    except AssertionError:
        print("Incorrect value.")

    # Test to ensure sum_series is returning the correct value for the correct
    #  sequence.
    # Fibonacci value.
    assert (sum_series(10) == 55)
    assert (sum_series(10, 2, 1 == 123))
