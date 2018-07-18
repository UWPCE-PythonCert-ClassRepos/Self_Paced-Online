"""
Return the fibonacci or lucas series of n length.

functions:
fibonacci(n) - Return the fibonacci series of n length.
lucas(n) - Return the lucas series of n length.
sum_series(n, x, y) - Generlization used by fibonaci(n) and lucas(n).
"""

def fibonacci(n):
    """Return the nth number in the fibonacci series"""
    fibval = sum_series(n, 0, 1)
    print(fibval)
    return fibval

def lucas(n):
    """Return the nth number in the lucas series."""
    lucval = sum_series(n, 2, 1)
    print(lucval)
    return lucval

def sum_series(n, x = 0, y = 1):
    """Return the nth number in the fibonacci (default) or lucas series.

    Generlization used by fibonaci(n) and lucas(n).

Parameters
----------
n : int
    Defines the fibonacci or lucas serie number to be returned.
x : int, optional (default = 0)
    Is the int at the 0 index of the fibonacci or lucas series.
y : int, optional (default = 1)
    Is the int at the 1 index of the fibonacci or lucas series.
    """

    lst = []
    # Append the list at the i index
    for i in range(n):
        if(i == 0):
            lst.append(x)
        elif(i == 1):
            lst.append(y)
        elif(i > 1):
            lst.append((lst[i - 2] + lst[i - 1]))
        nth = lst[i]
    return nth



def series_test():
    '''
    Each of the assertions below checks a different position in the
    fibonnacci or lucas series created by the functions above. The
    check is ran by providing a known position and respective value
    in the respective series.
    '''
    print ("First fibonaccie #:")
    assert fibonacci(1) == 0, "Fisrt fibonaccie # did not return 0"
    print ("Second fibonaccie #:")
    assert fibonacci(2) == 1, "Second fibonaccie # did not return 1"
    print ("Fifteenth fibonaccie #:")
    assert fibonacci(15) == 377, "Fifteenth fibonaccie # did not return 337"
    print ("First lucas #:")
    assert lucas(1) == 2, "First lucas # did not retrun 2"
    print ("Second lucas #:")
    assert lucas(2) == 1, "Second lucas # did not return 1"
    print ("Fifteenth lucas #:")
    assert lucas(15) == 843, "Fifteenth lucas # did not retrun 843"
