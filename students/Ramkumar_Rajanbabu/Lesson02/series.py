#Fibonacci Series

def fibonacci(n):    
    """Compute the nth Fibonacci number. 

    Args:
        n (int): the number of terms.
    Returns: 
        nth (int): the nth value in fibonacci series.
    
    """
    
    if (n < 0):
        print("Please enter a postive integer for n.")
    elif (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        nth = fibonacci(n-1) + fibonacci(n-2)
        return nth

def lucas(n):
    """Compute the nth Lucas number. 

    Args:
        n (int): the number of terms.
    Returns: 
        nth (int): the nth value in lucas series.
    
    """
    
    if (n < 0):
        print("Please enter a postive integer for n.")
    elif (n == 0):
        return 2 #Initial number different from fibonacci series
    elif (n == 1):
        return 1 #Same number as fibonacci series
    else:
        nth = lucas(n-1) + lucas(n-2)
        return nth

def sum_series(n, n0=0, n1=1):
    """Compute the nth value of a summation series.
    
    Args:
        n (int): the number of terms.
        n0 (int): the value of the zeroth element in the series.
        n1 (int): the value of the first element in the series. 
    Returns: 
        nth (int): the nth value in summation series.
        
    """
    
    if (n < 0):
        print("Please enter a postive integer for n.")
    elif (n == 0):
        return n0
    elif (n == 1):
        return n1
    else:
        nth = sum_series(n-1, n0, n1) + sum_series(n-2, n0, n1)
        return nth  
    
if __name__ == "__main__":
    #Run some tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29

    assert sum_series(0) == 0
    assert sum_series(1) == 1
    assert sum_series(2) == 1
    assert sum_series(3) == 2
    assert sum_series(4) == 3
    assert sum_series(5) == 5
    assert sum_series(6) == 8
    assert sum_series(7) == 13
    
    assert sum_series(0,2,1) == 2
    assert sum_series(1,2,1) == 1
    assert sum_series(2,2,1) == 3
    assert sum_series(3,2,1) == 4
    assert sum_series(4,2,1) == 7
    assert sum_series(5,2,1) == 11
    assert sum_series(6,2,1) == 18
    assert sum_series(7,2,1) == 29
    
    assert sum_series(5) == fibonacci(5)

    #Test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    print("Tests passed!")
    
