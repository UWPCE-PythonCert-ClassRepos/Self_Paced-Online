def fibonacci(n):
    l = [0,1]
    commonfunction(l,n)
def lucas(n):
    l = [2,1]
    commonfunction(l,n)
def commonfunction(l,n):
    m=1
    while len(l)<n:
        y=l[m-1]+l[m]
        l.append(y)
        m+=1
    print(l[n-1])
def sum_series(n,a=0,b=1):
    l = []
    l.append(a)
    l.append(b)
    commonfunction(l,n)