"""
Goal: Write a program that prints the numbers from 1 to 100 inclusive.
But for multiples of three print “Fizz” instead of the number.
For the multiples of five print “Buzz” instead of the number.
For numbers which are multiples of both three and five print “FizzBuzz” instead.
"""

count = 1
while count <= 100:
    if (count % 3 == 0 and count % 5 == 0):
        print("FizzBuzz")
    elif (count % 3 == 0):
        print("Fizz")
    elif (count % 5 == 0):
        print("Buzz")
    else:
        print(count)
    count += 1