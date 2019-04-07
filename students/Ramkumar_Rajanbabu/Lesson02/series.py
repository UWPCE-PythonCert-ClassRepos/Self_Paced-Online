#Fibonacci Series

def fibonacci(n):
    """
    To print the nth value in fibonacci series based on n value.
    
    Arguements:
        n: number of terms(integer)
    
    Returns:
        nth: nth value in fibonacci series
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
    """
    To print the nth value in lucas series based on n value.
    
    Arguements:
        n: number of terms(integer)
    
    Returns:
        nth: nth value in lucas series
    """
    
    if (n < 0):
        print("Please enter a postive integer for n.")
    elif (n == 0):
        return 2
    elif (n == 1):
        return 1
    else:
        nth = lucas(n-1) + lucas(n-2)
        return nth

def sum_series(n, n1, n2):
    """
    To print the fibonacci or lucas series based on parameters.
    
    Arguements:
        n: number of terms(integer)
    
    Returns:
        nth: nth value
    """
    
    if (n < 0):
        print("Please enter a postive integer for n.")
    elif (n == 0):
        return n1
    elif (n == 1):
        return n2
    else:
        nth = sum_series(n-1) + sum_series(n-2)
        return nth