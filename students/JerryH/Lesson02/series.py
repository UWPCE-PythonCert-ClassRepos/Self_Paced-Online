def FiboSeries(n):
    """This function prints out the nth digit in the Fibonacci series."""

    fibo = [0,1]
    for i in range(2,n):
    x = fibo[i-2] + fibo[i-1]
    fibo.append(x)
    return fibo[n-1]
    #print(fibo) #prints the whole series

def Lucas(n):
    """This function prints out the nth digit in the Lucas series."""


    lu = [2,1]
    for i in range(2,n):
    x = lu[i-2] + lu[i-1]
    lu.append(x)
    return lucas[n-1]
    #print(lu) #prints the whole series

def sum_series(n, arg1 = 0, arg2 = 1):
    """The required parameter will determine which element in the series
    to print. The two optional parameters will have default values of 0
    and 1 and will determine the first two values for the series to be
    produced."""

    series = [arg1, arg2]
    for i in range(2,n):
    x = series[i-2] + series[i-1]
    series.append(x)
    return series[n-1]

# Test FiboSeries(n) is returning the expected value [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
assert FiboSeries(5) == 3
assert FiboSeries(10) == 34

# Test Lucas(n) is returning the expected value [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]
assert Lucas(3) == 3
assert Lucas(9) == 47

# Test sum_series is returning the expected value
assert sum_series(5) == 3
assert sum_series(9,2,1) == 47
