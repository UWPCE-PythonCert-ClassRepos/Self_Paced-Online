#Jon Cracolici
#Lesson 2 Series Problems
#UW Python Cert
def fibonacci(n):
    """Returns Fibonacci Sequence value at 'n' index, with indexing starting at 0.
       arg1 = n = index of the value you wish to be returned.
    """
    try:
        if n>=0 and (n%int(n)==0.0) == True:
            pass
        else:
            print('Please use a natural number')
            return
    except:
        print('Please use a natural number')
        return
    intcheck = int(n)
    if intcheck == 0:
        return 0
    elif intcheck == 1:
        return 1
    fsequence = list(range(intcheck+1))
    for i in fsequence[2:]:
        fsequence[i] = fsequence[i-1] + fsequence[i-2]
    return fsequence[intcheck]
fibonacci(6)
def lucas(n):
    """Returns Lucas Sequence value at 'n' index, with indexing starting at 0.
       arg1 = n = index of the value you wish to be returned.
    """ 
    try:
        if n>=0 and (n%int(n)==0.0) == True:
            pass
        else:
            print('Please use a natural number')
            return
    except:
        print('Please use a natural number')
        return
    intcheck=int(n)
    if intcheck == 0:
        return 2
    elif intcheck == 1:
        return 1
    lsequence = list(range(intcheck+1))
    lsequence[0]=2
    for i in lsequence[2:]:
        lsequence[i] = lsequence[i-1] + lsequence[i-2]
    #print(lsequence[n])
    #print(lsequence)
    return lsequence[intcheck]
lucas(6)
def sum_series(n, a=0, b=1):
    """Returns the value of recursively additive seq at 'n' index,
    defaults to fibonacci. you may use kwargs 'a' and 'b' to set the 
    values of the first two indicies.
    arg1 = n = index of the value you wish to be returned.
    kwarg1 = a = value of sequence at index 0.
    kwarg2 = b = value of sequence at index 1.
    """
    try:
        if n>=0 and (n%int(n)==0.0) == True:
            pass
        else:
            print('Please use a natural number')
            return
    except:
        print('Please use a natural number')
        return
    intcheck = int(n)
    if intcheck == 0:
        return a
    elif intcheck == 1:
        return b
    sslist = list(range(intcheck+1))
    sslist[0] = a
    sslist[1] = b
    for i in sslist[2:]:
        sslist[i] = sslist[i-1] + sslist[i-2]
    return sslist[intcheck]
sum_series(6.5, a=2, b=1)
#This block of code is used to assert that the functions provide
#the correct answers for index = 6, and also that the sum_series
#function can create either the fibonacci or lucas series.

assert fibonacci(6)==8
assert lucas(6)==18
assert sum_series(6)==fibonacci(6)
assert sum_series(6, a=2, b=1)==lucas(6)