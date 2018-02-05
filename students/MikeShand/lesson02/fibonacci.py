def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

def luc(n):
    if n==1:
        return 2
    elif n==2:
        return 1
    else:
        return luc(n-1)+luc(n-2)

def seq(n,x=0, y=1):
    if n==1:
        return x
    elif n==2:
        return y
    else:
        return seq(n-1,x,y)+seq(n-2,x,y)



