import random
import timeit

def fibonacci_recursive(n):
    """
    Recursively compute the nth Fibonacci number (where n>1).
    The 0th fibonacci number is 0
    The 1st fibonacci number is 1
    The nth fibonacci number is the (n-2)th - (n-1)th fibonacci number.
    """
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci_recursive(n-2)+fibonacci_recursive(n-1)

def fibonacci(n):
    """
    Compute the nth fibonacci number with a loop (where n>1).
    The 0th fibonacci number is 0
    The 1st fibonacci number is 1
    The nth fibonacci number is the (n-2)th - (n-1)th fibonacci number
    """
    fibo = [0,1]
    lastFibo = 0
    if n > 1:
        for x in range(n-1):
            lastFibo = fibo[1]
            fibo[1] = fibo[0]+fibo[1]
            fibo[0] = lastFibo
    else:
        return fibo[n]
    return fibo[1]

def lucas(n):
    """
    Compute the nth lucas number with a loop (where n>1).
    The 0th Lucas number is 2
    The 1st lucas number is 1
    The nth lucas number is the (n-2)th - (n-1)th lucas number
    """
    luca = [2,1]
    lastLuca = 0
    if n > 1:
        for x in range(n-1):
            lastLuca = luca[1]
            luca[1] = luca[0]+luca[1]
            luca[0] = lastLuca
    else:
        return luca[n]
    return luca[1]

def sum_series(n, zeroth=0, first=1):
    """
    Compute the nth sum in the series with a loop (where n>1).
    The 0th sum series number is zeroth
    The 1st sum series number is first
    The nth sum series number is the (n-2)th - (n-1)th sum series number
    """
    series = [zeroth,first]
    swap = 0
    if n > 1:
        for x in range(n-1):
            swap = series[1]
            series[1] = series[0]+series[1]
            series[0] = swap
    else:
        return series[n]
    return series[1]

def testing(n=10):
    #First 10 Fibonacci numbers for assert statements
    fibonacciNums = [0,1,1,2,3,5,8,13,21,34,55]
    #First 10 Lucas numbers for assert statements
    lucasNums = [2,1,3,4,7,11,18,29,47,76,123]
    #First 10 numbers of sum series starting w/ 12 and 7
    weird  = [12,7,19,26,45,71,116,187,303,490,793]

    #Check fibonacci_recursive fxn returns the correct fibo numbers
    start = timeit.default_timer()
    print('The first '+str(n)+' fibonacci numbers (starting at 0): recursively')
    for x in range(n):
        assert fibonacci_recursive(x)==fibonacciNums[x]
        print(fibonacci_recursive(x), end=', ')
    assert fibonacci_recursive(n)==fibonacciNums[n]
    print(fibonacci_recursive(n))
    print(timeit.default_timer()-start, end='\n\n')
    

    #Check fibonacci fxn returns the correct fibo numbers
    start = timeit.default_timer()
    print('The first '+str(n)+' fibonacci numbers (starting at 0): w/ a loop')
    for x in range(n):
        print(fibonacci(x), end=', ')
        assert fibonacci(x)==fibonacciNums[x]
    assert fibonacci(n) == fibonacciNums[n]
    print(fibonacci(n))
    print(timeit.default_timer()-start,end='\n\n')

    #Check lucas fxn returns the correct lucas numbers
    print('The first '+str(n)+' lucas numbers (starting at 0): w/ a loop')
    for x in range(n):
        assert lucas(x)==lucasNums[x]
        print(lucas(x), end=', ')
    assert lucas(n)==lucasNums[n]
    print(lucas(n),end='\n\n')

    #Check default sum_series fxn returns fibonacci numbers
    print('The first '+str(n)+' fibo nums w/ sum_series')
    for x in range(n):
        assert sum_series(x)==fibonacciNums[x]
        print(sum_series(x), end=', ')
    assert sum_series(n)==fibonacciNums[n]
    print(sum_series(n),end='\n\n')

    #Check sum_series w/ lucas parameters returns lucas series
    print('The first '+str(n)+' lucas nums w/ sum_series')
    for x in range(n):
        assert sum_series(x,2,1)==lucasNums[x]
        print(sum_series(x,2,1), end=', ')
    assert sum_series(n,2,1)==lucasNums[n]
    print(sum_series(n,2,1),end='\n\n')

    #Check sum_series w/ 12,7 as first 2 elements returns correct series
    print('The first '+str(n)+' weird nums w/ sum_series: 12,7')
    for x in range(n):
        assert sum_series(x,12,7)==weird[x]
        print(sum_series(x,12,7), end=', ')
    assert sum_series(n,12,7)==weird[n]
    print(sum_series(n,12,7),end='\n\n')


testing()
testing(7)
