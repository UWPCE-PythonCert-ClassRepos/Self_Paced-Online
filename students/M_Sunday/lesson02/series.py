# lesson 02 - Fibonacci and Lucas Series


def fibonacci(n):
    """
    This function inputs an integer, n, and returns the nth value
    of the fibonacci series, where n is the integer entry

    :param n: Integer input value

    :return: nth value in fibonacci series
    """
    if n == 1:
        val = 1
    else:
        val = 0
    val_p = 1
    val_pp = 0

    for i in range(n-1):
        if n == 0:
            val = 0
        elif n == 1:
            val = 1
        else:
            val = val_pp + val_p
            val_pp = val_p
            val_p = val

    return val


# print(fibonacci(7))


def lucas(n):
    """
    This function inputs an integer, n, and returns the nth value
    of the lucas series, where n is the integer entry

    :param n: Integer input value

    :return: nth value in fibonacci series
    """
    if n == 0:
        val = 2
    else:
        val = 1
    val_p = 1
    val_pp = 2
    for i in range(n-1):
        if n == 0:
            val = 2
        elif n == 1:
            val = 1
        else:
            val = val_pp + val_p
            val_pp = val_p
            val_p = val
    return val


# print(lucas(5))


def series(n, first=0, second=1):
    """
    This function inputs the following integers and returns
    the nth value of the fibonacci series which the first two
    series values being those the user defines, where n is the
    integer entry.

    :param n: Integer input value for series index to return
    :param first: Integer input value for first series value
                  Default value = 0
    :param second: Integer input value for second series value
                   Default value = 1

    :return: nth value in series
    """
    if n == 0:
        val = first
    else:
        val = second
    val_p = second
    val_pp = first
    for i in range(n-1):
        if n == 0:
            val = 2
        elif n == 1:
            val = 1
        else:
            val = val_pp + val_p
            val_pp = val_p
            val_p = val
    return val


# print(series(7, 2, 1))


# Tests
def verify(case, tester, output):
    """
    This function takes a function input and compares it with an
    expected output value, for a specific test case ID. The
    function returns None if there is no failure and returns a
    failure message if there is a failure

    :param case: Input case number
    :param tester: Input function to evaluate
    :param output: Expected output from input function

    :return: success
    """
    if tester == output:
        pass
    else:
        print("FAIL: Test case", case, "input does not return expected output of", output)


# This tests the fibonacci function
verify(1, fibonacci(0), 0)
verify(2, fibonacci(1), 1)
verify(3, fibonacci(2), 1)
verify(4, fibonacci(3), 2)
verify(5, fibonacci(4), 3)
verify(6, fibonacci(5), 5)
verify(7, fibonacci(6), 8)
verify(8, fibonacci(7), 13)

# This test2 the lucas series
verify(9, lucas(0), 2)
verify(10, lucas(1), 1)
verify(11, lucas(2), 3)
verify(12, lucas(3), 4)
verify(13, lucas(4), 7)
verify(14, lucas(5), 11)
verify(15, lucas(6), 18)
verify(16, lucas(7), 29)

# This tests the custom series by utilizing the fibonacci and lucas
# functions where possible
verify(17, series(0), fibonacci(0))
verify(18, series(1), fibonacci(1))
verify(19, series(2), fibonacci(2))
verify(20, series(3), fibonacci(3))
verify(21, series(4), fibonacci(4))
verify(22, series(5), fibonacci(5))
verify(23, series(6), fibonacci(6))
verify(24, series(7), fibonacci(7))
verify(25, series(0, 2, 1), lucas(0))
verify(26, series(1, 2, 1), lucas(1))
verify(27, series(2, 2, 1), lucas(2))
verify(28, series(3, 2, 1), lucas(3))
verify(29, series(4, 2, 1), lucas(4))
verify(30, series(5, 2, 1), lucas(5))
verify(31, series(6, 2, 1), lucas(6))
verify(32, series(7, 2, 1), lucas(7))
verify(33, series(0, 57, 102), 57)
verify(34, series(1, 57, 102), 102)
verify(35, series(2, 57, 102), 159)
verify(36, series(3, 57, 102), 261)
