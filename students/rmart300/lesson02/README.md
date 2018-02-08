Lesson 2 assignment by Ross Martin

fizz_buzz.py

•A program that prints the numbers from 1 to 100 inclusive.
•But for multiples of three print “Fizz” instead of the number.
•For the multiples of five print “Buzz” instead of the number.
•For numbers which are multiples of both three and five print “FizzBuzz” instead.

series.py

def fibonnaci(n)
The Fibonacci Series is a numeric series starting with the integers 0 and 1.
In this series, the next integer is determined by summing the previous two.
This gives us:
0, 1, 1, 2, 3, 5, 8, 13, ...

def lucas(n)
The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1. The resulting series looks like this:
2, 1, 3, 4, 7, 11, 18, 29, ...
In your series.py module, add a new function, lucas, that returns the nth value in the lucas numbers series.
Ensure that your function has a well-formed docstring.

def sum_series(n,x=0,y=1)
The required parameter will determine which element in the fibonacci or lucas series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced, thereby driving wheer fibonacci or lucas series is used.  Fibonacci is used by default if x and y are not provided
