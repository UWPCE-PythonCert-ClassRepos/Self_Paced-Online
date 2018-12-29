def fibonacci(n):
    l = [0,1]
    m=1
    while len(l)<n:
        y=l[m-1]+l[m]
        l.append(y)
        m+=1
    print(l[n-1])
def lucas(n):
    l = [2,1]
    m=1
    while len(l)<n:
        y=l[m-1]+l[m]
        l.append(y)
        m+=1
    print(l[n-1])