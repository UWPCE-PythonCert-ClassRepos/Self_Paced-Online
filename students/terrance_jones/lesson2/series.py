def fibonacci(n):
    ''' Returns the nth element'''
    if n == 1:
	return 1
    elif n == 0:
	return 0
    else:
	return fibonacci(n-2) + fibonacci(n-1)


def lucas(n):
    ''' Returns the nth element'''
    if n == 1:
        return 1
    elif n == 0:
	return 2
    else:
	return lucas(n-2) + lucas(n-1)



def sum_series(n, a=0, b=1):
    ''' Returns the nth element. a and b are the first two elements'''
    if n == 1:
	return b
    elif n == 0:
	return a
    else:
	return sum_series(n-2, a ,b) + sum_series(n-1, a, b)


#Running test to make sure functions work
if __name__ == '__main__':
#Testing fibonacci function
    assert(fibonacci(1) == 1)
    assert(fibonacci(2)==1)
    assert(fibonacci(6)==8)
    	
#Testing lucas function
	
    assert(lucas(1) == 1)
    assert(lucas(2) == 3)
    assert(lucas(6) == 18)
    
#Testing sum_series w/ 1 argument eqsumuals fibonacci
    assert(sum_series(3) == fibonacci(3))
    assert(sum_series(5) == fibonacci(5))

    #Testing sum series w 2 and 1 arg
    assert(sum_series(3, 2, 1) == lucas(3))

    #Testing with different values
    assert(sum_series(3,4,5))== 14

    print("Testing Complete")
   