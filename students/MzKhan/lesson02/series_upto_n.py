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
    #print('The Fibonacci series for n = {}'.format(n))
    first, second = 0, 1
    if n == 0:
        return str(first)
    elif n == 1:
        return str(first)+','+str(second)
    series = [first,second]
    result = str(first)+','+str(second)
    for i in range(2,n+1):
        series.append(series[i-1] + series[i-2])
        result +=','+str(series[i])
    return result


 # The lucas series is an integer series starting with 2,1.
 # The next integer is determined by summing the previous two.
 # i.e: 2, 1, 3, 4, 7, 11, 18, 29, ...
 # The function returns the lucas series of the first n+1 terms.

def lucas(n):
    #print('The Lucas series for n = {}'.format(n))
    first, second = 2, 1
    if n == 0:
        return str(first)
    elif n == 1:
        return str(first)+','+str(second)
    series = [first,second]
    result = str(first)+','+str(second)
    for i in range(2,n+1):
        series.append(series[i-1] + series[i-2])
        result +=','+str(series[i])
    return result


# The General method that computes the Fibonacci series OR Lucas series.
# The required parameter is n.
# The default first = 0, second = 1 gives the Fibonacci series.
# The first =2, second=1 gives the Lucas series.

def sum_series(n,first=0, second = 1):
    if ( first == 0 and second == 1):
        return fibonacci(n)
    elif ( first == 2 and second == 1):
        return lucas(n)
    else:
        series = [first,second]
        result = str(first)+','+str(second)
        for i in range(2,n+1):
            series.append(series[i-1] + series[i-2])
            result +=','+str(series[i])
        return result




if __name__ == "__main__":
    print("Use assert statements to check Fibonacci Series: ")
    assert(int(fibonacci(0)) == 0 ) , "Error: Incorrect Fibonacci Series!"
    n=10
    checkFib = fibonacci(n).split(',')
    assert(int(checkFib[2]) == 1), "Error: Incorrect Fibonacci Series!"
    assert(int(checkFib[-1]) == 55), "Error: Incorrect Fibonacci Series!"
    assert(int(checkFib[5]) == 5), "Error: Incorrect Fibonacci Series!"
    print('Fibonacci Series Passed!!!')
    print()
    print("Use assert statements to check Lucas Series: ")
    checkFib = lucas(n).split(',')
    assert(int(checkFib[0]) == 2), "Error: Incorrect Fibonacci Series!"
    assert(int(checkFib[1]) == 1), "Error: Incorrect Fibonacci Series!"
    assert(int(checkFib[-1]) == 123), "Error: Incorrect Fibonacci Series!"
    print('Lucas Series Passed!!!')
    print()
    print('The Fibonacci series for n = {}\n{}'.format(n,fibonacci(n)))
    print()
    print('The Lucas series for n = {}\n{}'.format(n,lucas(n)))
    print()
    n=15
    print('The Lucas series for n = {}\n{}'.format(n,sum_series(n,second=1,first=2)))
    print()
    print('The Fibonacci series for n = {}\n{}'.format(n,sum_series(n,second=1,first=0)))
    print()
    print('The Other series for n = {}\n{}'.format(n,sum_series(n,second=2,first=2)))



