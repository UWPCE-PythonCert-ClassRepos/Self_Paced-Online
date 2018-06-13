import sys

#Function returns the nth value of the Fibonacci series
def Fibonacci(n):
    #Defined variables
    var1=0
    var2=1

    #if n reaches first Fibonacci value then return its value
    if n==var1:
        return var1
    #if n reaches second Fibonacci value then return its value
    elif n==var2:
        return var2
    else:
        #Surrounding with a try blcok to catch and return
        #any exceptions raised during execution
        try:
            #use recursion to return the sum of the previews two numbers
                return Fibonacci(n-2) + Fibonacci(n-1)
        except Exception as e:
            print(e.message)
            raise

#Function returns the nth value of the Lucas series
def Lucas(n):
    l0=2
    l1=1

    if n==0:
        return l0
    elif n==1:
        return l1
    else:
        #Surrounding with a try blcok to catch and return
        #any exceptions raised during execution
        try:
            return Lucas(n-1) + Lucas(n-2)
        except Exception as e:
            print(e.message)
            raise

#Function returns sum values based on the initial input
#Input: n -- nth value of the sum_series
#Optional: var1, var2 with default values 0,1
def sum_series(n, var1=0, var2=1):
    if n==0:
        return var1
    elif n==1:
        return var2
    else:
        #Surrounding with a try blcok to catch and return
        #any exceptions raised during execution
        try:
            return sum_series(n-1,var1, var2) + sum_series(n-2, var1, var2)
        except Exception as e:
            print(e.message)
            raise

#Fibonacci Test cases:
#Default value(0,1) should return numbers from the Fibonacci series
#Fibonacci series at index 0 is 0
assert 0 == sum_series(0)
#Fibonacci series at index 1 should return 1
assert 1 == sum_series(1)
#Fibonacci series at index 2 should return 1
assert 1 == sum_series(2)
#Fibonacci series at index 3 should return 2
assert 2 == sum_series(3)
#Fibonacci series at index 10 should return 55
assert 55 == sum_series(10)

#Lucas Test cases:
#Default value(0,1) should return numbers from the Fibonacci series
#Lucas at index 0 should return 2
assert 2 == sum_series(0,2,1)
#Lucas at index 1 should return 1
assert 1 == sum_series(1,2,1)
#Lucas at index 2 should return 3
assert 3 == sum_series(2,2,1)
#Lucas at index 3 should return 4
assert 4 == sum_series(3,2,1)
#Lucas at index 10 should return 123
assert 123 == sum_series(10,2,1)


#Other Series Test cases:
#Replacing the default values should return numbers from the other series
#This series uses 3 and 2 as default values
#Other series at index 0 should return 3
assert 3 == sum_series(0,3,2)
#Other series at index 1 should return 2
assert 2 == sum_series(1,3,2)
#Other series at index 2 should return 5
assert 5 == sum_series(2,3,2)
#Other series at index 3 should return 7
assert 7 == sum_series(3,3,2)
#Other series at index 10 should return 212
assert 212 == sum_series(10,3,2)
