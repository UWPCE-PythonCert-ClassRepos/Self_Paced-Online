def fibonacci(n):
    """Return the nth Fibonacci number."""
    
    if n == 0:
        return 0
    elif n == 1:
        return 1    
    else:
        return fibonacci(n-1) + fibonacci(n-2)
 
    
def lucas(n):
    """Return the nth Lucas number."""
    
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
    
    
def sum_series(n, term_0 = 0, term_1 = 1):
    """
    Return the nth value of a sequence in which term n is the sum of terms 
    (n-1) and (n-2).
    
    :param n:       the nth term in the sequence
    :param term_0:  the 0th term in the sequence
    :param term_1:  the first term in the sequence
    """
    
    if n == 0:
        return term_0
    elif n == 1:
        return term_1
    else:
        return sum_series(n-1,term_0,term_1) + sum_series(n-2,term_0,term_1)
    

####  Begin test block of code  #### 
    
# The first 8 terms in the fibonacci and lucas sequences    
fib_sequence = [0, 1, 1, 2, 3, 5, 8, 13]
lucas_sequence = [2, 1, 3, 4, 7, 11, 18, 29]

# Loop through the first 8 terms in the fibonacci sequence to test fibonacci(n)
for n, fibn in enumerate(fib_sequence):
    assert( fibonacci(n) == fibn)
    
# Loop through the first 8 terms in the lucas sequence to test lucas(n)
for n, lucn in enumerate(lucas_sequence):
    assert( lucas(n) == lucn)
    
# Check that the default values of sum_series() reproduce fibonacci() and that
# sum_series(n,2,1) returns the nth lucas number
for k in range(20):
    assert(fibonacci(k) == sum_series(k))
    assert(lucas(k) == sum_series(k,2,1))    