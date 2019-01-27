
'''
finbonancci function to return the nth value in the faibonacci series starting with zero index
'''
def fibonacci(n):
    '''
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result =fibonacci(n-2) + fibonacci(n-1)
    '''
    return sum_series(n)

'''
lucas function to return the nth value in the lucas series 
'''
def lucas(n):
    '''if n == 0:
        result = 2
    elif n == 1:
        result = 1
    else:
        result =lucas(n-2) + lucas(n-1)
    '''
    return sum_series(n, first=2, second=1)

'''
general function to return the nth element with given input params
if @param first == 0 and @param second ==1 then it return fibonacci
if @param first == 2 and @param second ==1 then it return lucas
'''
def sum_series(element, first=0, second=1):
    if element == 0:
        result = first
    elif element == 1:
        result = second
    else:
        result =sum_series(element-2, first, second) + sum_series(element-1, first, second)
    return result


####Test with assertion error to make sure lucas, fibonacci and sum_series return correct values############

assert (lucas(3) == 4)
assert (fibonacci(4) ==3)
assert(sum_series(4) == 3)
assert(sum_series(3, 2,1))