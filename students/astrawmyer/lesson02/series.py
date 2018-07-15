def fibonacci(n):
    """add a doc string"""
    a=0
    b=1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a=0
        b=1
        for i in range(n-2):
            c=a+b
            a=b
            b=c
        #print(i,c)
    print(c)

#fibonacci(8)


def lucas(n):
    """add a doc string"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a=2
        b=1
        for i in range(n-2):
            c=a+b
            a=b
            b=c
        #print(i,c)
    print(c)

#lucas(8)

def sum_series(n, a=0, b=1):
    #add a doc string
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        #a=2
        #b=1
        for i in range(n-2):
            c=a+b
            a=b
            b=c
        #print(i,c)
    print(c)

sum_series(8)