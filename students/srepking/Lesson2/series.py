def fibonacci(n):
    """Fibonacci Series 0,1,1,2,3...returning the nth number in the list starting with index 0."""  
    if n==0:
        return(0)
    if n==1:
        return(1)
    if n>1:
        return fibonacci(n-2)+fibonacci(n-1)
     

            
        
print(fibonacci(3))

def lucas(n):
    """Create a Lucas Series 2,1,3,4....and returns the nth value starting index 0."""
    if n==0:
        return(2)
    if n==1:
        return(1)
    if n>1:
        return lucas(n-2)+lucas(n-1)

print (lucas(3))