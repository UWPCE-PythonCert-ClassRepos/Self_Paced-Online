
def fibonacci(n):

    fib = [0] * (n+1)
    fib[0] = 0 
    fib[1] = 1
    
    for i in range(2, n + 1):        
        fib[i] =  fib[i-1] + fib[i-2]
    return(fib)


def lucas(n):

    luc = [0]*(n+1)
    luc[0] = 2
    luc[1] = 1
    
    for i in range(2, n+1):
        luc[i] = luc[i-2] + luc[i-1]
    return(luc)


def sum_series(n, n0 = 0, n1 =1):
    
    fib = [0] * (n+1)
    
    fib[0] = n0
    fib[1] = n1
    
    for i in range(2, n + 1):        
        fib[i] =  fib[i-1] + fib[i-2]
    return(fib)

