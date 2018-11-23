def fibonacci(n):
    # 0  1  2  3  4  5  6  7
    # 0, 1, 1, 2, 3, 5, 8, 13,
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
##------------------------

def lucas(n):
    # 0  1  2  3  4  5   6   7
    # 2, 1, 3, 4, 7, 11, 18, 29, ...

    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)
## -------------------------------

def sum_series(n_index, zero_index=0, one_index=1):
    '''
    sum_series() function requires one required parameter and two optional parameters.
    The required parameter will determine which element in the series to print
    The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.
    Calling this function with no optional parameters will produce numbers from the fibonacci series.
    Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers.
    Other values for the optional parameters will produce other series.
    '''

    if zero_index == 0 and one_index == 1:
        #fib
        # 0  1  2  3  4  5  6  7
        # 0, 1, 1, 2, 3, 5, 8, 13,
        if n_index == 0:
            return 0
        elif n_index == 1:
            return 1
        else:
            return sum_series(n_index - 1) + sum_series(n_index - 2)


    elif zero_index == 2 and one_index == 1:
        #lucas
        # 0  1  2  3  4  5   6   7
        # 2, 1, 3, 4, 7, 11, 18, 29, ...
        if n_index == 0:
            return 2
        elif n_index == 1:
            return 1
        else:
            return sum_series(n_index - 1, zero_index = 2, one_index = 1) + sum_series(n_index - 2, zero_index = 2, one_index = 1)

    else:
        #some other summing series
        # 0  1      2           3       4           5       6
        # 3,  1,    4,          5,      9,          14,     23
        z_idx = zero_index
        one_idx = one_index
        if n_index == 0:
            return zero_index
        elif n_index == 1:
            return one_index
        else:
            return sum_series(n_index - 1, zero_index = z_idx, one_index = one_idx) + sum_series(n_index - 2, zero_index = z_idx, one_index = one_idx)

    #-----------------------

assert (fibonacci(7)) == 13
assert (lucas(7)) == 29
assert (sum_series(7)) == 13  #asserting that when 2nd/3rd arg are not specified, it's fib series
assert (sum_series(2, zero_index = 100, one_index = 350)) == 450 # 100 + 350 = 450
print (sum_series.__doc__)