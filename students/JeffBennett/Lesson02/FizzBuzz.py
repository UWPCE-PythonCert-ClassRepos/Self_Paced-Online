"""
Write a program that prints the numbers from 1 to 100 inclusive.
But for multiples of three print "Fizz" instead of the number.
For the multiples of five print "Buzz" instead of the number.
For multiples of both three and five print "FizzBuzz" instead.
"""
for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        print(str(i) + " FizzBuzz")
    elif i % 5 == 0:
        print(str(i) + " Buzz")
    elif i % 3 == 0:
        print(str(i) + " Fizz")
    else:
        print(i)
