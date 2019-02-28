'''
    Name: Muhammad Khan
    Date: 02/12/2019
    Assignment02

'''
# Purpose:
# The Fibonacci Series is a numeric series starting with the integers 0 and 1.
# In this series, the next integer is determined by summing the previous two.
# i.e: 0, 1, 1, 2, 3, 5, 8, 13, ...
# The function returns the fibonacci series of the first n+1 terms..

def fibonacci(n):
    '''
    parm: int  an integer value > 0.
    return: int        nth term of the fibonacci series.
    '''
    #print('The Fibonacci series for n = {}'.format(n))
    return sum_series(n)


 # The lucas series is an integer series starting with 2,1.
 # The next integer is determined by summing the previous two.
 # i.e: 2, 1, 3, 4, 7, 11, 18, 29, ...
 # The function returns the lucas series of the first n+1 terms.

def lucas(n):
    '''
    parm: int    an integer value > 0
    return: int      nth term of the Lucas series.
    '''
    #print('The Lucas series for n = {}'.format(n))
    return sum_series(n,first=2,second=1)


# The General method that computes the Fibonacci series OR Lucas series.
# The required parameter is n.
# The default first = 0, second = 1 gives the Fibonacci series.
# The first =2, second=1 gives the Lucas series.

def sum_series(n,first=0, second = 1):
    '''
    parm: int      required.
    parm: first = 0   defalult kwarg argument.
    park: second = 1   default kwarg argument.
    return: int        nth term of the fibonacci series (default)
           OR nth term of the Lucas series IF first=2, second=1
           OR nth term of other series.
    '''
    series = [first,second]
    if n == 0:
        return series[0]
    elif n == 1:
       return series[-1]
    for i in range(2,n+1):
        series.append(series[i-1] + series[i-2])
    return series[-1]




if __name__ == "__main__":
    print("Use assert statements to check Fibonacci Series: ")
    assert(fibonacci(0) == 0 ) , "Error: Incorrect Fibonacci Series!"
    n=10

    assert(fibonacci(1) == 1), "Error: Incorrect Fibonacci Series!"
    assert(fibonacci(n) == 55), "Error: Incorrect Fibonacci Series!"
    assert(fibonacci(5) == 5), "Error: Incorrect Fibonacci Series!"
    print('Fibonacci Series Passed!!!')
    print()
    print("Use assert statements to check Lucas Series: ")
    assert(lucas(0) == 2), "Error: Incorrect Fibonacci Series!"
    assert(lucas(1) == 1), "Error: Incorrect Fibonacci Series!"
    assert(lucas(n) == 123), "Error: Incorrect Fibonacci Series!"
    print('Lucas Series Passed!!!')
    print()
    print('The n = {}th term of the Fibonacci series: {}'.format(n,fibonacci(n)))
    print()
    print('The n = {}th term of the Lucas series: {}'.format(n,lucas(n)))
    print()
    n=15
    print('The n = {}th term of the Lucas series: {}'.format(n,sum_series(n,second=1,first=2)))
    print()
    print('The n = {}th term of the Fibonacci series: {}'.format(n,sum_series(n,second=1,first=0)))
    print()
    print('The n = {}th term of the Other series: {}'.format(n,sum_series(n,second=2,first=2)))



