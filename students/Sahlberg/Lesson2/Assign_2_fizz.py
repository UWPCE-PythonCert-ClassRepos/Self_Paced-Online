"""Ian Sahlberg
Python 210
Assignment 2 FizzBuzz
12/22/2018"""

for num in range(1, 101):

    if num%3 == 0 and num%5 == 0:

        print('FizzBuzz')

    elif num%3 ==0:

        print('Fizz')

    elif num%5 ==0:

        print('Buzz')

    else:

        print(num)