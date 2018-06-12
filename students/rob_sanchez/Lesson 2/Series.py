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
        except Exception as ex:
            print(ex.message)
            raise

#def Lucas(n):
    #next function

#def sum_series(n, optional, optional):
