# -*- coding: utf-8 -*-
"""
Created on Thu Jan 3 21:52:08 2019
@author: Florentin Popescu
"""

#============LESSON_02====================
# Fibonaci and Lucas numbers exercise-----
#=========================================

#-----------------------------------------
# PART A - Fibonaci numbers
#-----------------------------------------

# Option 1 - Iterative 'for' loop & using a cache for numbers
def fibonacci(n):
    x, y = 0, 1
    for i in range(0, n):
        x, y = y, x + y
    return x

%timeit fibonacci(10) + fibonacci(25) + fibonacci(50)
#11.4 µs ± 22.9 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
#-----------------------------------------

# Option 2 - Simple recursive Fibonacci; no gardians, no memoization
def fibonaci(n):
    # base case
    if n == 0:
        return 0
    elif n ==1:
        return 1
    # recursive case
    else: return fibonaci(n-1) + fibonaci(n-2)
        
%timeit fibonacci(10) + fibonacci(25) + fibonacci(50)
# 11.3 µs ± 51.9 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
#------------------------------------------

# Option 3 - Simple recursive Fibonacci with try-except, no storage
def fibonaci(n):
    try: 
        n >= 0
    except Exception as err:
        print("typo error: enter an argument >= 0 " + str(err))
    
    # base case
    if n == 0:
        return 0
    elif n ==1:
        return 1
    # recursive case
    else: return fibonaci(n-1) + fibonaci(n-2)
        
%timeit fibonacci(10) + fibonacci(25) + fibonacci(50)
# 11.2 µs ± 76.5 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
#-------------------------------------------

# Option 4 - Memoized Fibonacci with gardians and pull from storage
base_case = {0:0, 1:1}
def fibonacci(n):
    # gardians
    if not isinstance(n, int):
        print('Fibonacci numbers are defined for integeres')
        return None
    elif n < 0:
        print ('Fibonacci numbers are not defined for negative integers')
        return None
    # base case
    if n in base_case: 
        return base_case[n]
    # recursive case
    fib = fibonacci(n-1) + fibonacci(n-2)
    base_case[n] = fib
    return fib

%timeit fibonacci(10) + fibonacci(25) + fibonacci(50)
#1.84 µs ± 12.9 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
#-------------------------------------------

# Option 5 - Fibonacci via generating a list & picking last element
def fibonacci(n):
    # gardians
    if not isinstance(n, int):
        print('Fibonacci numbers are defined for integeres')
        return None
    elif n < 0:
        print ('Fibonacci numbers are not defined for negative integers')
        return None
    #generate a list of 2 elements for the base case
    fib = []
    fib.append(0)
    fib.append(1)
    #generate a local list of fibonaci numbers
    for i in range(1, n):
        fib.append(fib[-1] + fib[-2])
        i += 1
    return fib[-1] # last element in the list (fib[n])

%timeit fibonacci(10) + fibonacci(25) + fibonacci(50)
#34.7 µs ± 303 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
#The disadvantage is that when we compute a new fibonaci we re-create the list 
#---------------------------------------------

# Option 6 -My prefered Fibonacci; append and use list mutability
fibonacci = []
fibonacci.append(0)
fibonacci.append(1)
    
# generate a large list with 100 Fiboncaci numbers
for i in range(1, 100):
   fibonacci.append(fibonacci[-1] + fibonacci[-2])
   i += 1

%timeit fibonacci[10] + fibonacci[25] + fibonacci[50]
#1 ns ± 4.36 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

'''
Advantages of Option 6:
    - fastest
    - new fibonaci element is computed by adding two elements in a list
    - the list can be stored as aseparate fle and used for any purposes
    - any fibonacy number can be accessed simply indexing its number in list
    - one can do computation usig many elements of the list at once whithot 
      recomputing each one separately

Examples:
    accesing fibonacci numbers:
        print(fibonacci[3])

    # statistics with fibonacci list fibonacci
        sum_100_fibonacci = np.array(fibonacci).sum()
        mean_100_fibonacci = np.array(fibonacci).mean()
        var_100_fibonacci = np.array(fibonacci).var()
        std_100_fibonacci = np.array(fibonacci).std()

    summary statistics
        pd.DataFrame(fib).describe()
'''

#-----------------------------------------
# PART B - Lucas numbers
#-----------------------------------------
 
# Option 1 - recursive with gardians and external storage
base_case = {0:2, 1:1}
def lucas(n):
    # gardians
    if not isinstance(n, int):
        print('Lucas numbers are defined for integeres')
        return None
    elif n < 0:
        print ('Lucas numbers are not defined for negative integers')
        return None
    # base cases 
    if n in base_case: 
        return base_case[n]
    # recurrsive case 
    luc = lucas(n - 1) + lucas(n - 2)
    base_case[n] = luc
    return luc
    
%timeit lucas(10) + lucas(25) + lucas(50)
#1.86 µs ± 11 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

#-----------------------------------------
# PART C - Generalization
#-----------------------------------------

# Option 1 - recursive with gardians, no memoization
def sum_series(n, a = 0, b  = 1):
    #-----------------------------
    # gardians
    if not isinstance(n, int):
        print('Fibonacci and Lucas numbers are defined for integeres')
        return None
    elif n < 0:
        print ('Fibonacci and Lucas numbers are not defined for negative integers')
        return None
    #-----------------------------   
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        return sum_series(n-1, a, b) + sum_series(n-2, a, b)

%timeit sum_series(10) + sum_series(25) + sum_series(50)
#takes very long time to compute sum_series(50)
#-----------------------------------------------

# Option 2 - recursive with gardians and memoization
base_case = {0:0, 1:1}
base_case_l = {0:2, 1:1}

def sum_series(n, a = base_case[0], b = base_case[1]):
    # gardians
    if not isinstance(n, int):
        print('Fibonacci and Lucas numbers are defined for integeres')
        return None
    elif n < 0:
        print ('Fibonacci and Lucas numbers are not defined for negative integers')
        return None
    if a == base_case[0] and b == base_case[1]:
        if n in base_case: 
            return base_case[n]
        # recurrsive case 
        res = sum_series(n - 1, a, b) + sum_series(n - 2, a, b)
        base_case[n] = res
        return res
    
    if a == base_case_l[0] and b == base_case_l[1]:
        if n in base_case_l: 
           return base_case_l[n]
        # recurrsive case 
        res = sum_series(n - 1, a, b) + sum_series(n - 2, a, b)
        base_case_l[n] = res
        return res
    else: 
        print("base case coresponds to other series")
        return None

%timeit sum_series(10) + sum_series(25) + sum_series(50)
#2.98 µs ± 27.9 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

%timeit sum_series(10, 2, 1) + sum_series(25, 2, 1) + sum_series(50, 2, 1)
#3.33 µs ± 14.7 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
#============================================
# END
#============================================