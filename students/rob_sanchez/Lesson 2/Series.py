import sys

#Function returns the nth value of the fibonacci series
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

#Function returns the nth value of the fibonacci series
def Lucas(n):
    l0=2
    l1=1

    if n==0:
        return l0
    elif n==1:
        return l1
    else:
        try:
            return Lucas(n-1) + Lucas(n-2)
        except Exception as e:
            print(e.message)
            raise

#Function returns values based on the initial input
#Input: n -- nth value of the sum_series
#Optional: opt1, opt2
def sum_series(n, var1=0, var2=1):
    if n==0:
        return var1
    elif n==1:
        return var2
    else:
        return sum_series(n-1,var1, var2) + sum_series(n-2, var1, var2)

#Test cases
print "Test(Fibonacci): sum_series(0) Output:", sum_series(0)
print "Test(Fibonacci): sum_series(1) Output:", sum_series(1)
print "Test(Fibonacci): sum_series(2) Output:", sum_series(2)
print "Test(Fibonacci): sum_series(3) Output:", sum_series(3)
print
print "Test(Lucas): sum_series(0,2,1) Output:", sum_series(0,2,1)
print "Test(Lucas): sum_series(1,2,1) Output:", sum_series(1,2,1)
print "Test(Lucas): sum_series(2,2,1) Output:", sum_series(2,2,1)
print "Test(Lucas): sum_series(3,2,1) Output:", sum_series(3,2,1)
print
print "Test(Fibonacci): sum_series(10) Output:", sum_series(10)
print
print "Test(Lucas): sum_series(10,2,1) Output:", sum_series(10,2,1)
print
print "Test(Other): sum_series(0,3,2) Output:", sum_series(0,3,2)
print "Test(Other): sum_series(1,3,2) Output:", sum_series(1,3,2)
print "Test(Other): sum_series(2,3,2) Output:", sum_series(2,3,2)
print "Test(Other): sum_series(3,3,2) Output:", sum_series(3,3,2)
print "Test(Other): sum_series(10,3,2) Output:", sum_series(10,3,2)
