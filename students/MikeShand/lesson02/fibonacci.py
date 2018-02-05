def fibo(n):
    """Returns the nth element of the fibonacci sequence"""
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

def luc(n):
    """Returns the nth element of the lucas sequence"""
    if n==1:
        return 2
    elif n==2:
        return 1
    else:
        return luc(n-1)+luc(n-2)

def seq(n,x=0, y=1):
    """Returns the nth element of a user defined sequence, 
     The parameters x and y define the first two elements of 
      the sequence"""
    if n==1:
        return x
    elif n==2:
        return y
    else:
        return seq(n-1,x,y)+seq(n-2,x,y)


#I'll now run a few tests using "assert" to make sure these work
#I'm sure there's an easier way to do this!

assert fibo(1)==0 
assert fibo(2)==1
assert fibo(3)==1
assert fibo(4)==2
assert fibo(5)==3
assert fibo(6)==5
assert fibo(7)==8
assert fibo(8)==13

assert luc(1)==2
assert luc(2)==1
assert luc(3)==3
assert luc(4)==4
assert luc(5)==7
assert luc(6)==11
assert luc(7)==18
assert luc(8)==29

assert seq(1)==fibo(1)
assert seq(2)==fibo(2)
assert seq(3)==fibo(3)
assert seq(4)==fibo(4)
assert seq(5)==fibo(5)
assert seq(6)==fibo(6)
assert seq(7)==fibo(7)
assert seq(8)==fibo(8)
assert seq(9)==fibo(9)

assert seq(1,2,1)==luc(1)
assert seq(2,2,1)==luc(2)
assert seq(3,2,1)==luc(3)
assert seq(4,2,1)==luc(4)
assert seq(5,2,1)==luc(5)
assert seq(6,2,1)==luc(6)
assert seq(7,2,1)==luc(7)
assert seq(8,2,1)==luc(8)
assert seq(9,2,1)==luc(9)