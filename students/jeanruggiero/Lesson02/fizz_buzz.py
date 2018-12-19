#!/usr/bin/env python3

# This is a program that prints the numbers from 1 to 100 inclusive.
# But for multiples of three print “Fizz” instead of the number.
# For the multiples of five print “Buzz” instead of the number.
# For numbers which are multiples of both three and five print “FizzBuzz” instead.

for n in range(1,101):
    if not n % 15: # Find multiples of 3 and 5
        print('FizzBuzz')
    elif not n % 3: # Next find multiples of 3
        print('Fizz')
    elif not n % 5: # Finally find multiples of 5
        print('Buzz')
    else:
        print(n) # If not a multiple of 3 or 5, print the number
