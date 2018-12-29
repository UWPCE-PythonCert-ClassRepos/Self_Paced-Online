def fibonacci(n):
    l = [0,1]
    commonfunction(l,n)
    return l
def lucas(n):
    l = [2,1]
    commonfunction(l,n)
    return l
def commonfunction(l,n):
    m=1
    while len(l)<n:
        y=l[m-1]+l[m]
        l.append(y)
        m+=1
    print(l[n-1])
    return l
def sum_series(n,a=0,b=1):
    l = []
    l.append(a)
    l.append(b)
    commonfunction(l,n)
    return l

assert fibonacci(5)==[0,1,1,2,3],"The Program Returned an Incorrect Sequence for the Fibonacci Function Test"
assert lucas(5)==[2,1,3,4,7],"The Program Returned an Incorrect Sequence for the Lucas Function Test"
assert sum_series(3)==fibonacci(3),"The Default Output for sum_series was NOT Fibonacci"
assert sum_series(3,2,1)==lucas(3),"The Lucas Configured sum_series Returned an Incorrect Sequence"