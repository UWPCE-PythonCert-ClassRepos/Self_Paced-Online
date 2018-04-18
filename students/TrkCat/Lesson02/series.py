#Module for number series (Fibonacci, Lucas)

def fibonacci(n):
    """Return nth value of Fibonacci series"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
        

def lucas(n):
    """Return nth value of Lucas series"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)
        
        
def sum_series(n, a=0, b=1):
    """Return nth value of additive series starting with [a, b]"""
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return sum_series(n-2,a,b) + sum_series(n-1,a,b)
        
        
if __name__ == "__main__":
    #Testing fibonacci function for initial values and 7th value
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(7) == 13
    
    #Testing lucas function for initial values and 7th value
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(7) == 29
    
    #Testing sum_series function for initial values
    assert sum_series(0, a=5) == 5
    assert sum_series(1, b=5) == 5
    
    #Testing sum_series function for 7th fib and lucas numbers
    assert sum_series(7,0,1) == 13
    assert sum_series(7,2,1) == 29
    
    print('All tests successful')