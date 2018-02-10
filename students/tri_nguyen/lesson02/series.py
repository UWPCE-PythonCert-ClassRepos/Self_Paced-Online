# -------------------------------------------#
# Student:   Tri Nguyen
# Instructor: Natasha Aleksandrova
# Date:  02-Feb-2018
# -------------------------------------------#

def fibonacci(n):
    ''' this function will compute the Fibonacci series '''
    
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
               
def lucas(num):
    ''' this function will compute the Lucas numbers
        that start with values 2 and 1
    '''
    
    if num == 0:
        return 2
    elif num == 1:
        return num
    else:
        return lucas(num - 1) + lucas(num - 2)
        
def sum_series(num, op_one = 0, op_two = 1):
    ''' 
        Calling this function with no optional parameters
        will produce numbers from the fibonacci series
        Call it with the optional arguments 2 and 1 will
        produce values from the lucas numbers. Other values
        for optional parameters will produce other series
    '''
    
    if not isinstance(num, int):
        print('Please enter only integers.')
        return None
    elif num < 0:
        print('Negative numbers are not allowed.')
        return None
    elif num == 0:
        return op_one
    elif num == 1:
        return op_two
    else:
        return sum_series(num - 1, op_one, op_two) + sum_series(num - 2, op_one, op_two)
                

# Testing

# Call function fibonacci() and sum_series() without optional
# parameters defined should produce the same result

assert fibonacci(5) == sum_series(5)

# Call function fibonacci() and sum_series() with optional
# arguments defined should produce the same result

assert fibonacci(5) == sum_series(5, 0, 1)

# Call function lucas() and sum_series() with optional
# arguments defined as 2 and 1 should produce the same result

assert lucas(7) == sum_series(7, 2, 1)

# Print out results
print('Call fibonacci(6)', '-->', fibonacci(6))
print('Call sum_series(6)', '-->', sum_series(6))

print('Call lucas(11)', '-->', lucas(11))
print('Call sum_series(11, 2, 1)', '-->', sum_series(11, 2, 1))