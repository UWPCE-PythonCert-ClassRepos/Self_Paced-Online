def fibonacci(n):
    """
        fibonacci recursive -  the function will call itself with decreasing n values until n=0; the computer is building an internal
        memory stack with each function; after n=0 is reach each function is the sum of the previous function return values
    """
    if n == 0:
        return 0
    elif  n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """
        lucas recursive -  the function will call itself with decreasing n values until n=0;
        difference between lucas and fibonacci are different returned values at n=0
    """
    if n == 0:
        return 2
    elif  n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

def sum_series(n,a=0, b=1):
    """
        generalization of fibonacci and lucas fuctions; a=0 for fibonacci; a=2 for lucas; b=1 for fibonacci and lucas;
        the function allows to enter any a, b values
    """
    #print (n,a,b)
    if n==0:
        return a
    elif n==1:
        return b
    else:
        return sum_series(n-1,a,b) + sum_series(n-2,a,b)

if __name__=="__main__":
    print ("start testing")

    assert fibonacci(6)==8
    assert lucas(6)==18
    #use default parameters - same as fibonacci
    assert sum_series(6)==8
    #change a=2 parameter - same as lucas
    assert sum_series(6,2)==18

    print ("test complete")
