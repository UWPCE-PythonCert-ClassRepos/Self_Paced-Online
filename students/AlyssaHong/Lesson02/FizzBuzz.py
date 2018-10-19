"""
Author: Alyssa Hong
Date: 10/15/2018
Lesson2 Assignments > The Classic Fizz Buzz Problem
"""

# Goal : Write a program that prints the numbers from 1 to 100 inclusive.
#        But for multiples of three print “Fizz” instead of the number.
#        For the multiples of five print “Buzz” instead of the number.
#        For numbers which are multiples of both three and five print “FizzBuzz” instead.

#changed function: while --> for in range()

for i in range(1,100):
    if i % 3 == 0 and i % 5 ==0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
