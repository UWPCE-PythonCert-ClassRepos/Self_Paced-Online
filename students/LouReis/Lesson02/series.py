# series.py
# Fibonacci assignment
# Coded by LouReis
#
# Note that the fibinacci series is naturally recursive –
# the value is defined by previous values:
# fib(n) = fib(n-2) + fib(n-1)
#

def fibonacci(n):
    for x in range(0,n):
        n=(n-2) + (n-1)
    print(n)

def user_input():
#This function prompts the user for the square size & grid dimensions.
  print ('This function returns the nth value in the fibonacci series.')
  n=int(input('Enter the value for n: '))
  print('The',n'th','value is:')
  fibonacci(n)

user_input()
