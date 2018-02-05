
#this is the function that computer fibonacci and return the nth value
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

#this is the function that computer lucas and return the nth value
def lucas(n):
    if n==1:
        return 2
    elif n==2:
        return 1
    return lucas(n-2) + lucas(n-1)

#this is the generalizing function
def sum_series(n,a=0, b=1):
    if n==1:
        return a
    elif n==2:
        return b
    return sum_series(n-2,a,b) + sum_series(n-1,a,b)

#in following line, all three function will be tested by a for loop
# and be print it out to inform the observer


fiblist = [0, 1, 1, 2, 3, 5, 8, 13] #make a list following fibonacci
for i in range(1,8):  #using a for loop to check fibonacci function
    assert fibonacci(i) == fiblist[i-1]

lucaslist = [2, 1, 3, 4, 7, 11, 18, 29] #make a list following lucas
for i in range(1,8): #using a for loop to check lucas function
    assert lucas(i) == lucaslist[i-1]

fiblist = [0, 1, 1, 2, 3, 5, 8, 13]
lucaslist = [2, 1, 3, 4, 7, 11, 18, 29]
for i in range(1,8): #using a for loop to check sum_series function
    assert sum_series(i) == fiblist[i-1]
for i in range(1,8): #using a for loop to check sum_series function has optional parameters
    assert sum_series(i,2,1) == lucaslist[i-1]
