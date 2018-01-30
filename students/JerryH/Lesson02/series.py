def fibo_series(n):
    """This function prints out the nth digit in the Fibonacci series."""

    fibo = [0,1]
    for i in range(2,n+1):
        x = fibo[i-2] + fibo[i-1]
        fibo.append(x)
    return fibo[n]
    #print(fibo) #prints the whole series

def lucas_series(n):
    """This function prints out the nth digit in the Lucas series."""

    lu = [2,1]
    for i in range(2,n+1):
        x = lu[i-2] + lu[i-1]
        lu.append(x)
    return lu[n]
    #print(lu) #prints the whole series

def sum_series(n, arg1 = 0, arg2 = 1):
    """The required parameter will determine which element in the series
    to print. The two optional parameters will have default values of 0
    and 1 and will determine the first two values for the series to be
    produced."""

    series = [arg1, arg2]
    for i in range(2,n+1):
        x = series[i-2] + series[i-1]
        series.append(x)
    return series[n]

# Test fibo_series(n) is returning the expected value [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
assert fibo_series(5) == 5
assert fibo_series(10) == 55

# Test lucas_series(n) is returning the expected value [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]
assert lucas_series(3) == 4
assert lucas_series(9) == 76

# Test sum_series is returning the expected value
assert sum_series(5) == 5
assert sum_series(9,2,1) == 76
