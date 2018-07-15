def fibonacci(n):
    #add a doc string
    a=0
    b=1
    for i in range(n-2):
        c=a+b
        a=b
        b=c
        #print(i,c)
    print(c)

fibonacci(8)


def lucas(n):
    #add a doc string
    a=2
    b=1
    for i in range(n-2):
        c=a+b
        a=b
        b=c
        #print(i,c)
    print(c)

lucas(8)